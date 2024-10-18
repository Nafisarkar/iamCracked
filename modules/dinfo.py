import psutil
import json
import os

def get_device_info():
    # Get system information
    device_username = os.getlogin()
    cpu_info = psutil.cpu_times()._asdict()
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()._asdict()

    # Get memory information
    mem_info = psutil.virtual_memory()._asdict()
    total_ram_gb = mem_info['total'] / (1024 ** 3)  # Convert bytes to GB

    # Get disk information
    disk_partitions = psutil.disk_partitions()
    disk_usage = []
    for partition in disk_partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage.append({
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'fstype': partition.fstype,
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent
        })

    # Get network information
    net_io_counters = psutil.net_io_counters()._asdict()
    net_connections = [conn._asdict() for conn in psutil.net_connections()]

    # Get battery information (if available)
    try:
        battery_info = psutil.sensors_battery()._asdict()
    except:
        battery_info = None

    # Get running software information
    running_software = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            if proc.status() == psutil.STATUS_RUNNING:
                running_software.append({
                    'pid': proc.pid,
                    'name': proc.name()
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return {
        'device_username': device_username,
        'cpu_info': cpu_info,
        'cpu_count': cpu_count,
        'cpu_freq': cpu_freq,
        'total_ram_gb': total_ram_gb,
        'disk_usage': disk_usage,
        'net_io_counters': net_io_counters,
        'net_connections': net_connections,
        'battery_info': battery_info,
        'running_software': running_software
    }

def main():
    device_info = get_device_info()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, 'dinfo.txt')
    with open(output_file, 'w') as f:
        json.dump(device_info, f, indent=4)
    print(f"Device information has been written to {output_file}")

if __name__ == '__main__':
    main()