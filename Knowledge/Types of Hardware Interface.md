202510021732
Status: #permanent
Tags:

# Types of Hardware Interface
## Embedded / MCU-Level Interfaces
### GPIO (General Purpose Input/Output)
| Aspect      | Characteristics                                        |
| ----------- | ------------------------------------------------------ |
| Type        | Point-to-point                                         |
| Element     |                                                        |
| Concept     | Simple digital input/output pins (ON/OFF, slow/simple) |
| Application | button, LED, relay, trigger                            |

![[Pasted image 20251002183117.png|400]]

### I2C (Inter-Integrated Circuit)
| Aspect      | Characteristics                                                |
| ----------- | -------------------------------------------------------------- |
| Type        | Shared bus                                                     |
| Element     | - 2-wire serial bus (SDA = data, SCL = clock)<br>- Half-duplex |
| Concept     |                                                                |
| Application | Sensors (accelerometers, temperature), EEPROMs                 |

![[Pasted image 20251002183333.png|500]]

### SPI (Serial Peripheral Interface)
| Aspect      | Characteristics                                             |
| ----------- | ----------------------------------------------------------- |
| Type        | Shared bus                                                  |
| Element     | - 4-wire serial bus (MISO, MOSI, SCLK, CS)<br>- Full-duplex |
| Concept     |                                                             |
| Application | Displays, flash memory, high-speed sensors                  |

### UART (Universal Asynchronous Receiver/Transmitter)
| Aspect      | Characteristics                                     |
| ----------- | --------------------------------------------------- |
| Type        | Point-to-point                                      |
| Element     | - 2-wire asynchronous serial communication (TX, RX) |
| Concept     |                                                     |
| Application | Debug console, GPS, Bluetooth                       |

### Others
- **RS-232**: embedded and industrial devices

## High-Speed System Interfaces
### PCI (Peripheral Component Interconnect)
| Aspect      | Characteristics                        |
| ----------- | -------------------------------------- |
| Type        | Shared bus                             |
| Element     | - Parallel bus (legacy)                |
| Concept     |                                        |
| Application | Older GPUs, network cards, sound cards |

### PCIe (Peripheral Component Interconnect Express)
| Aspect      | Characteristics                                                                     |
| ----------- | ----------------------------------------------------------------------------------- |
| Type        | Point-to-point                                                                      |
| Concept     | - Scalable serial bus lanes, each with RX and TX (x1, x4, x8, x16)<br>- Full-duplex |
| Application | GPUs, SSDs, NICs, AI accelerators                                                   |

### USB (Universal Serial Bus)
| Aspect      | Characteristics                           |
| ----------- | ----------------------------------------- |
| Type        | Shared bus                                |
| Concept     | - Differential signaling<br>- Half-duplex |
| Application | Keyboards, mice, storage, charging        |

### Others
- **SATA / NVMe**: Storage
- **Ethernet**: Network
- **HDMI / DisplayPort**: Display

## Automotive / Industrial Interfaces
- **CAN (Controller Area Network):** Cars, drones, robotics
- **LIN (Local Interconnect Network):** Low-cost automotive bus
- **FlexRay:** High-speed automotive safety-critical bus
- **Modbus / Profibus:** Industrial automation

## Memory Interfaces
- **DDR / LPDDR:** System RAM (desktop/mobile)
- **GDDR:** Graphics memory (GPU)
- **HBM (High Bandwidth Memory):** AI/HPC accelerators

## Specialized / Miscellaneous Interfaces
- **MIPI (Mobile Industry Processor Interface):** Cameras, displays
- **JTAG:** Chip debugging and testing
- **Thunderbolt:** High-speed data + display + power (PCIe + DisplayPort)
- **QSFP / CFP:** Optical networking modules

---
# References
