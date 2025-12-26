---
Topics:
---
202512191116
Status: #permanent
Tags: [[computer]], [[hardware]]

# Elements of Hardware Interface
## Data
### Physical path
- Dedicated data – physical wire carries data bits directly
- Differential data – data carried on two complementary wires, with the signal interpreted from the difference between the two wires

### Data representation
- Encoded data – data, clock, control and framing are encoded together into a single data stream
- Raw/binary data – data is sent directly as high/low voltage levels

### Data flow
- Half duplex – data travel both ways but only one direction at a time
- Full duplex – data travel in both directions at the same time (faster)

## Clock/Timing
- Dedicated clock wire
- Clock embedded in data
- Clock recovered via Phase-Locked Loop

```ad-info
This aspect differentiates between synchronous transmission and asynchronous transmission. Synchronous transmission require clock wire. See [[Hardware Interfaces#Concept#Synchronous/Synchronous Transmission]].

```

## Addressing/ Device selection
1. Address inside data
	1. Dynamic address – assign through enumeration
	2. Fixed address – predefined
2. Chip select wire
3. Point-to-point (no address)

```ad-info
This aspect differentiates between shared bus and point-to-point types of hardware interface. Point-to-point interface does not use address. See [[Hardware Interfaces#Concept#Shared Bus/Point-to-point]]

```

## Control
1. Control wires
2. Control bits (encoded inside data)

**Other Aspect**:
1. Protocol frame
2. Electrical behaviour

## Power & Ground
**Power**
1. Separate power wires
	- power provided from bus
	- external supply
2. Phantom power – power supplied over the same wire used for signal transmission

**Ground**
1. Shared ground
2. Separate ground

---
# References
