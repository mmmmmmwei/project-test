---
Topics:
---
202512191406
Status: #permanent
Tags: [[computer]], [[hardware]]

# Concept of Hardware Interface
## 1.1 Master/Slave
**Master**
- Device that initiates actions, controls timing, send commands.
- CPU, controller

**Slave**
- Device that respond to the master's commands.
- External device

*In modern interface, devices can act as both master and slave.*

## 1.2 Shared Bus/Point-to-point
**Shared bus**
- Multiple devices share a single communication path
- Only 1 device can communicate at a time
- Need addressing (see [[Elements of Hardware Interface#Addressing/ Device selection]])

**Point-to-Point**
- Dedicated link exists between 2 devices
- Communication is direct, simultaneous, independent of other links
- No addressing (see [[Elements of Hardware Interface#Addressing/ Device selection]])

## 1.3 Serial Bus/Parallel Bus
**Serial bus**
- Send bits one after another on fewer wires.

**Parallel bus**
- Send multiple bits simultaneously in individual wires
- Signals on different wires might arrive at different times and cause error.

## 1.4 Half Duplex/Full Duplex
**Half-duplex**
- Data travel both ways but only one direction at a time.
- Share 1 wire

**Full-duplex**
- Data travel in both directions at the same time (faster).
- Need 2 wires

## 1.5 Synchronous/Synchronous Transmission
![[Hardware Interfaces.png|400]]
See [[Elements of Hardware Interface#Clock/Timing]]

---
# References
