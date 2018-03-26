import psutil


def cpu():
    return {
        "count": psutil.cpu_count(),
        "load": psutil.cpu_percent(interval=1, percpu=True)
    }


def mem():
    mem_obj = psutil.virtual_memory()
    return {
        "total": mem_obj.total,
        "available": mem_obj.available,
        "free": mem_obj.free,
        "percent": mem_obj.percent
    }


def disks():
    parts = psutil.disk_partitions()
    ret = {}
    for part in parts:
        vals = psutil.disk_usage(part.mountpoint)
        ret[part.device] = {
            'total': vals.total,
            'used': vals.used,
            'free': vals.free
        }

    return ret


def status():
    return {
        "cpu": cpu(),
        "mem": mem(),
        "disk": disks()
    }
