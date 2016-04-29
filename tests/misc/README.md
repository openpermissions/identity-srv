compare_uuid_generators.py
==========================

compare_uuid_generators.py scripts generates and gauge how long it takes to
generate 10K, 50K, 100K UUIDs using four UUID generators provided in the
Python's standard library.

Generator description
=====================
uuid.uuid1([node[, clock_seq]])
    Generate a UUID from a host ID, sequence number, and the current time. If node is not given, getnode() is used to obtain the hardware address. If clock_seq is given, it is used as the sequence number; otherwise a random 14-bit sequence number is chosen.

uuid.uuid3(namespace, name)
    Generate a UUID based on the MD5 hash of a namespace identifier (which is a UUID) and a name (which is a string).

uuid.uuid4()
    Generate a random UUID.

uuid.uuid5(namespace, name)
    Generate a UUID based on the SHA-1 hash of a namespace identifier (which is a UUID) and a name (which is a string).

To get the results simply:
=========================
    python compare_uuid_generators.py

Example results
===============
This was run on a virtual box with 2GB of ram and dual core CPU:


It took 1.58316993713 to generate 10000 UUID5 based on UUId1 and UUID4.urn.Avg time to gen one UUID: 0.000158316993713
It took 7.57234191895 to generate 50000 UUID5 based on UUId1 and UUID4.urn.Avg time to gen one UUID: 0.000151446838379
It took 15.108782053 to generate 100000 UUID5 based on UUId1 and UUID4.urn.Avg time to gen one UUID: 0.00015108782053
It took 1.50424909592 to generate 10000 UUID3 based on UUId1 and UUID4.urn.Avg time to gen one UUID: 0.000150424909592
It took 7.61191010475 to generate 50000 UUID3 based on UUId1 and UUID4.urn.Avg time to gen one UUID: 0.000152238202095
It took 15.0050089359 to generate 100000 UUID3 based on UUId1 and UUID4.urn.Avg time to gen one UUID: 0.000150050089359
It took 0.669743061066 to generate 10000 UUID1.Avg time to gen one UUID: 6.69743061066e-05
It took 3.35457086563 to generate 50000 UUID1.Avg time to gen one UUID: 6.70914173126e-05
It took 6.67676115036 to generate 100000 UUID1.Avg time to gen one UUID: 6.67676115036e-05
It took 0.406669139862 to generate 10000 UUID4.Avg time to gen one UUID: 4.06669139862e-05
It took 1.95403385162 to generate 50000 UUID4.Avg time to gen one UUID: 3.90806770325e-05
It took 4.15825390816 to generate 100000 UUID4.Avg time to gen one UUID: 4.15825390816e-05
