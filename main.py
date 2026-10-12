#***************************************************
# MSSV: 20248977
# Họ và tên:  Đào Quý Sang
#***************************************************
from abc import ABC, abstractmethod
from enum import Enum


# 1. Device Status Enumeration
class DeviceStatus(Enum):
    ACTIVE = "Active"
    UNDER_MAINTENANCE = "UnderMaintenance"
    RETIRED = "Retired"


# 2. Network Capability Interface
class INetworkable(ABC):
    @abstractmethod
    def connect(self, ip_address):
        pass

    @abstractmethod
    def disconnect(self):
        pass


# 3. Abstract Base Class for Devices
class Device(ABC):
    def __init__(self, device_id, name, year_of_use, price, status=DeviceStatus.ACTIVE):
        self.device_id = device_id
        self.name = name
        self.year_of_use = year_of_use
        self.price = price
        self.status = status

    @abstractmethod
    def annual_maintenance_cost(self):
        pass


# 4. Computer Derived Class
class Computer(Device, INetworkable):
    def __init__(self, device_id, name, year_of_use, price, ram_gb, cpu, has_gpu, status=DeviceStatus.ACTIVE):
        super().__init__(device_id, name, year_of_use, price, status)
        self.ram_gb = ram_gb
        self.cpu = cpu
        self.has_gpu = has_gpu

    def annual_maintenance_cost(self):
        # Maintenance cost calculation logic to be implemented
        return 0.0

    def connect(self, ip_address):
        pass

    def disconnect(self):
        pass


# 5. Printer Derived Class
class Printer(Device):
    def __init__(self, device_id, name, year_of_use, price, printer_type, pages, is_color=False, status=DeviceStatus.ACTIVE):
        super().__init__(device_id, name, year_of_use, price, status)
        self.printer_type = printer_type
        self.pages = pages
        self.is_color = is_color

    def annual_maintenance_cost(self):
        # Maintenance cost calculation logic to be implemented
        return 0.0


# 6. Network Printer Derived Class
class NetworkPrinter(Printer, INetworkable):
    def __init__(self, device_id, name, year_of_use, price, printer_type, pages, is_color=False, status=DeviceStatus.ACTIVE):
        super().__init__(device_id, name, year_of_use, price, printer_type, pages, is_color, status)

    def connect(self, ip_address):
        pass

    def disconnect(self):
        pass


# 7. Projector Derived Class
class Projector(Device):
    def __init__(self, device_id, name, year_of_use, price, lumens, lamp_hours, status=DeviceStatus.ACTIVE):
        super().__init__(device_id, name, year_of_use, price, status)
        self.lumens = lumens
        self.lamp_hours = lamp_hours

    def annual_maintenance_cost(self):
        # Maintenance cost calculation logic to be implemented
        return 0.0


# 8. Laboratory Room Aggregation Class
class LabRoom:
    def __init__(self, room_id, name, capacity):
        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_id):
        pass

    def annual_maintenance_cost(self):
        return 0.0


def main():
    print("Project structure and base class skeletons initialized successfully.")


if __name__ == "__main__":
    main()