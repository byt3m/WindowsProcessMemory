from memory import *

m = Memory()

process = "process.exe"

# Getting Base Address
pyHandle = m.GetProcessHandle(process, 1)
modules = m.EnumModules(pyHandle)
BaseAddress = modules[0]

# Address to read from or write to
Addr =  BaseAddress + 0x3B7A2A4

# Getting handle for reading and writting
cHandle = m.GetProcessHandle(process, 0)

# Start reading and writting, check the memory.py to find the function you need.