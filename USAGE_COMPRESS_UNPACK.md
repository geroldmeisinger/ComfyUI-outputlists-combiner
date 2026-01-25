# OutputLists Compress & Unpack - Usage Guide

## Overview

These two nodes enable **multi-parameter iteration** with inspire-pack's ForeachList nodes. They solve the problem of iterating through multiple synchronized values (e.g., CFG + sampler_name) in a single loop.

## The Problem

`CombineOutputLists` generates Cartesian products with **separate outputs**:
- `unzip_a`: `[7.0, 7.0, 7.5, 7.5, 8.0, 8.0]`
- `unzip_b`: `["euler", "dpm++", "euler", "dpm++", "euler", "dpm++"]`

But `ForeachListBegin` only accepts a **single ITEM_LIST** input, so you can't pass both at the same time.

## The Solution

**OutputLists Compress** packs multiple lists into tuples → **OutputLists Unpack** extracts them inside the loop.

---

## Example Workflow: CFG × Sampler Sweep

### Step 1: Create Lists

```
[Number OutputList]
  start: 7.0
  stop: 8.0
  num: 3
  → float: [7.0, 7.5, 8.0]

[String OutputList]
  values: "euler, dpm++"
  → string: ["euler", "dpm++"]
```

### Step 2: Generate Combinations

```
[OutputLists Combinations]
  list_a ← [7.0, 7.5, 8.0]
  list_b ← ["euler", "dpm++"]
  → unzip_a: [7.0, 7.0, 7.5, 7.5, 8.0, 8.0]
  → unzip_b: ["euler", "dpm++", "euler", "dpm++", "euler", "dpm++"]
  → count: 6
```

### Step 3: Compress into ITEM_LIST

```
[OutputLists Compress]
  list_a ← unzip_a
  list_b ← unzip_b
  → item_list: [(7.0, "euler"), (7.0, "dpm++"), (7.5, "euler"), ...]
  → count: 6
```

### Step 4: Start Loop

```
[ForeachListBegin] (inspire-pack)
  item_list ← item_list from Compress
  → flow_control
  → remained_list
  → item: (7.0, "euler")  ← This is a tuple!
  → intermediate_output
```

### Step 5: Unpack Tuple

```
[OutputLists Unpack]
  packed_item ← item from ForeachListBegin
  → value_a: 7.0
  → value_b: "euler"
  → value_c: None
  → value_d: None
```

### Step 6: Use Values in Workflow

```
[KSampler]
  cfg ← value_a (7.0)
  sampler_name ← value_b ("euler")
  model ← ...
  positive ← ...
  negative ← ...
  latent_image ← ...
  → LATENT
```

### Step 7: Save and Loop

```
[VAE Decode]
  samples ← LATENT from KSampler
  vae ← ...
  → IMAGE

[Save Image]
  images ← IMAGE
  filename_prefix: "cfg_sweep"

[ForeachListEnd] (inspire-pack)
  flow_control ← flow_control from Begin
  remained_list ← remained_list from Begin
  intermediate_output ← IMAGE
  → Loops back to Step 4 with next tuple (7.0, "dpm++")
```

---

## Complete Node Chain

```
Number OutputList → ┐
                    ├→ OutputLists Combinations → OutputLists Compress → ForeachListBegin
String OutputList → ┘                                                           │
                                                                                 ↓
                                                                          OutputLists Unpack
                                                                                 │
                                                                                 ↓
                                                                            KSampler
                                                                                 │
                                                                                 ↓
                                                                            VAE Decode
                                                                                 │
                                                                                 ↓
                                                                            Save Image
                                                                                 │
                                                                                 ↓
                                                                          ForeachListEnd
                                                                          (loops or finishes)
```

---

## Advanced: 3 or 4 Parameters

You can iterate through up to **4 synchronized parameters**:

```
[OutputLists Combinations]
  list_a ← CFG values
  list_b ← Sampler names
  list_c ← Step counts
  list_d ← Denoise strengths
  → 4 synchronized outputs

[OutputLists Compress]
  list_a ← unzip_a
  list_b ← unzip_b
  list_c ← unzip_c
  list_d ← unzip_d
  → item_list: [(7.0, "euler", 20, 0.8), ...]

[OutputLists Unpack]
  → value_a: 7.0
  → value_b: "euler"
  → value_c: 20
  → value_d: 0.8
```

---

## Notes

- **All input lists to Compress must have the same length** (guaranteed by OutputLists Combinations)
- **Unpack always outputs 4 values** - unused ones will be `None`
- **Compatible with any ITEM_LIST consumer**, not just ForeachList
- **The KSampler (or any other node) remains completely unmodified**

---

## Troubleshooting

**Q: ForeachListBegin shows an error about ITEM_LIST type**  
A: Make sure you're connecting the `item_list` output from Compress, not the individual lists.

**Q: Unpack outputs are all None**  
A: Check that you're connecting the `item` output from ForeachListBegin, not `remained_list`.

**Q: Loop only runs once**  
A: Ensure `remained_list` from Begin is connected to End, and `flow_control` is connected with rawLink.

**Q: Can I use more than 4 parameters?**  
A: Not with the current implementation. You'd need to create a custom node or nest multiple loops.

