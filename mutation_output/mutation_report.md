# Encoders.py Mutation Testing Report

**Total mutants generated:** 143

## Mutation Testing Results

- **Killed:** 134 (93%)
- **Survived:** 9 (6%)
- **Errors:** 0
- **Timeouts:** 0
- **Mutation Score:** 93%

## Mutation Operators Summary

| Operator | Count | Killed | Survived | Description |
|----------|-------|--------|----------|-------------|
| AOR | 2 | 2 | 0 | Arithmetic Operator Replacement |
| CDL | 15 | 9 | 6 | Constant Replacement |
| DCI | 2 | 2 | 0 | Dictionary/Container Operations |
| FCR | 12 | 12 | 0 | Function Call Replacement |
| IOD | 3 | 3 | 0 | In/Not in Operator |
| LCR | 9 | 7 | 2 | Logical Connector Replacement |
| MSI | 10 | 10 | 0 | Method Call Modification |
| RIL | 48 | 48 | 0 | Return Statement Mutation |
| ROR | 11 | 10 | 1 | Relational Operator Replacement |
| TYP | 16 | 16 | 0 | Type Check Mutation |
| UOI | 15 | 15 | 0 | Unary Operator Insertion |

## Results by Routine/Function

| Routine | Total | Killed | Survived |
|---------|-------|--------|----------|
| decimal_encoder | 14 | 14 | 0 |
| generate_encoders_by_class_tuples | 6 | 6 | 0 |
| isoformat | 3 | 3 | 0 |
| jsonable_encoder | 120 | 111 | 9 |

## Survived Mutants (For Analysis)

These mutants were not killed by tests and need investigation:

### Mutant #13 - ROR

**Routine:** `jsonable_encoder`  
**Line:** 277  
**Description:** Replace 'is not' with 'is' at line 277

**Original:**
```python
and (value is not None or not exclude_none)
```

**Mutated:**
```python
and (value is None or not exclude_none)
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---

### Mutant #18 - LCR

**Routine:** `jsonable_encoder`  
**Line:** 274  
**Description:** Replace 'or' with 'and' at line 274

**Original:**
```python
or (not isinstance(key, str))
```

**Mutated:**
```python
and (not isinstance(key, str))
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---

### Mutant #21 - LCR

**Routine:** `jsonable_encoder`  
**Line:** 277  
**Description:** Replace 'or' with 'and' at line 277

**Original:**
```python
and (value is not None or not exclude_none)
```

**Mutated:**
```python
and (value is not None and not exclude_none)
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---

### Mutant #25 - CDL

**Routine:** `jsonable_encoder`  
**Line:** 137  
**Description:** Replace 'None,' with '{},' at line 137

**Original:**
```python
] = None,
```

**Mutated:**
```python
] = {},
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---

### Mutant #32 - CDL

**Routine:** `jsonable_encoder`  
**Line:** 178  
**Description:** Replace '= False' with '= True' at line 178

**Original:**
```python
] = False,
```

**Mutated:**
```python
] = True,
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---

### Mutant #33 - CDL

**Routine:** `jsonable_encoder`  
**Line:** 178  
**Description:** Replace 'False,' with 'True,' at line 178

**Original:**
```python
] = False,
```

**Mutated:**
```python
] = True,
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---

### Mutant #34 - CDL

**Routine:** `jsonable_encoder`  
**Line:** 187  
**Description:** Replace 'None,' with '{},' at line 187

**Original:**
```python
] = None,
```

**Mutated:**
```python
] = {},
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---

### Mutant #35 - CDL

**Routine:** `jsonable_encoder`  
**Line:** 199  
**Description:** Replace '= True' with '= False' at line 199

**Original:**
```python
] = True,
```

**Mutated:**
```python
] = False,
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---

### Mutant #36 - CDL

**Routine:** `jsonable_encoder`  
**Line:** 199  
**Description:** Replace 'True,' with 'False,' at line 199

**Original:**
```python
] = True,
```

**Mutated:**
```python
] = False,
```

**Analysis Required:** Determine if this is an equivalent mutant or if a new test is needed.

---


## All Mutants (Detailed)

### Mutant #1

- **Operator:** AOR
- **Routine:** generate_encoders_by_class_tuples
- **Line:** 104
- **Status:** KILLED
- **Description:** Replace '+' with '-' at line 104

**Original Code:**
```python
encoders_by_class_tuples[encoder] += (type_,)
```

**Mutated Code:**
```python
encoders_by_class_tuples[encoder] -= (type_,)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #1)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #2

- **Operator:** AOR
- **Routine:** jsonable_encoder
- **Line:** 269
- **Status:** KILLED
- **Description:** Replace '-' with '+' at line 269

**Original Code:**
```python
allowed_keys -= set(exclude)
```

**Mutated Code:**
```python
allowed_keys += set(exclude)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #2)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #3

- **Operator:** ROR
- **Routine:** decimal_encoder
- **Line:** 61
- **Status:** KILLED
- **Description:** Replace '>=' with '>' at line 61

**Original Code:**
```python
if isinstance(exponent, int) and exponent >= 0:
```

**Mutated Code:**
```python
if isinstance(exponent, int) and exponent > 0:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #3)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #4

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 221
- **Status:** KILLED
- **Description:** Replace 'is' with 'is not' at line 221

**Original Code:**
```python
if include is not None and not isinstance(include, (set, dict)):
```

**Mutated Code:**
```python
if include is not not None and not isinstance(include, (set, dict)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #4)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #5

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 221
- **Status:** KILLED
- **Description:** Replace 'is not' with 'is' at line 221

**Original Code:**
```python
if include is not None and not isinstance(include, (set, dict)):
```

**Mutated Code:**
```python
if include is None and not isinstance(include, (set, dict)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #5)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #6

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 223
- **Status:** KILLED
- **Description:** Replace 'is' with 'is not' at line 223

**Original Code:**
```python
if exclude is not None and not isinstance(exclude, (set, dict)):
```

**Mutated Code:**
```python
if exclude is not not None and not isinstance(exclude, (set, dict)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #6)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #7

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 223
- **Status:** KILLED
- **Description:** Replace 'is not' with 'is' at line 223

**Original Code:**
```python
if exclude is not None and not isinstance(exclude, (set, dict)):
```

**Mutated Code:**
```python
if exclude is None and not isinstance(exclude, (set, dict)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #7)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #8

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 266
- **Status:** KILLED
- **Description:** Replace 'is' with 'is not' at line 266

**Original Code:**
```python
if include is not None:
```

**Mutated Code:**
```python
if include is not not None:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #8)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #9

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 266
- **Status:** KILLED
- **Description:** Replace 'is not' with 'is' at line 266

**Original Code:**
```python
if include is not None:
```

**Mutated Code:**
```python
if include is None:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #9)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #10

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 268
- **Status:** KILLED
- **Description:** Replace 'is' with 'is not' at line 268

**Original Code:**
```python
if exclude is not None:
```

**Mutated Code:**
```python
if exclude is not not None:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #10)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #11

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 268
- **Status:** KILLED
- **Description:** Replace 'is not' with 'is' at line 268

**Original Code:**
```python
if exclude is not None:
```

**Mutated Code:**
```python
if exclude is None:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #11)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #12

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 277
- **Status:** KILLED
- **Description:** Replace 'is' with 'is not' at line 277

**Original Code:**
```python
and (value is not None or not exclude_none)
```

**Mutated Code:**
```python
and (value is not not None or not exclude_none)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #12)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #13

- **Operator:** ROR
- **Routine:** jsonable_encoder
- **Line:** 277
- **Status:** SURVIVED
- **Description:** Replace 'is not' with 'is' at line 277

**Original Code:**
```python
and (value is not None or not exclude_none)
```

**Mutated Code:**
```python
and (value is None or not exclude_none)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #13)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #14

- **Operator:** LCR
- **Routine:** decimal_encoder
- **Line:** 61
- **Status:** KILLED
- **Description:** Replace 'and' with 'or' at line 61

**Original Code:**
```python
if isinstance(exponent, int) and exponent >= 0:
```

**Mutated Code:**
```python
if isinstance(exponent, int) or exponent >= 0:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #14)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #15

- **Operator:** LCR
- **Routine:** jsonable_encoder
- **Line:** 213
- **Status:** KILLED
- **Description:** Replace 'or' with 'and' at line 213

**Original Code:**
```python
custom_encoder = custom_encoder or {}
```

**Mutated Code:**
```python
custom_encoder = custom_encoder and {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #15)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #16

- **Operator:** LCR
- **Routine:** jsonable_encoder
- **Line:** 221
- **Status:** KILLED
- **Description:** Replace 'and' with 'or' at line 221

**Original Code:**
```python
if include is not None and not isinstance(include, (set, dict)):
```

**Mutated Code:**
```python
if include is not None or not isinstance(include, (set, dict)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #16)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #17

- **Operator:** LCR
- **Routine:** jsonable_encoder
- **Line:** 223
- **Status:** KILLED
- **Description:** Replace 'and' with 'or' at line 223

**Original Code:**
```python
if exclude is not None and not isinstance(exclude, (set, dict)):
```

**Mutated Code:**
```python
if exclude is not None or not isinstance(exclude, (set, dict)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #17)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #18

- **Operator:** LCR
- **Routine:** jsonable_encoder
- **Line:** 274
- **Status:** SURVIVED
- **Description:** Replace 'or' with 'and' at line 274

**Original Code:**
```python
or (not isinstance(key, str))
```

**Mutated Code:**
```python
and (not isinstance(key, str))
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #18)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #19

- **Operator:** LCR
- **Routine:** jsonable_encoder
- **Line:** 275
- **Status:** KILLED
- **Description:** Replace 'or' with 'and' at line 275

**Original Code:**
```python
or (not key.startswith("_sa"))
```

**Mutated Code:**
```python
and (not key.startswith("_sa"))
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #19)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict FAILED                  [  4%]

================================== FAILURES ===================================
______________________________ test_encode_dict _______________________________
tests\test_jsonable_encoder.py:77: in test_encode_dict
    assert jsonable_encoder(pet) == {"name": "Firulais", "owner": {"name": "Foo"}}
E   AssertionError: assert {} == {'name': 'Fir...name': 'Foo'}}
E     
E     Right contains 2 more items:
E     {'name': 'Firulais', 'owner': {'name': 'Foo'}}
E     
E     Full diff:
E     + {}
E     - {...
E     
E     ...Full output truncat
```
</details>

---

### Mutant #20

- **Operator:** LCR
- **Routine:** jsonable_encoder
- **Line:** 277
- **Status:** KILLED
- **Description:** Replace 'and' with 'or' at line 277

**Original Code:**
```python
and (value is not None or not exclude_none)
```

**Mutated Code:**
```python
or (value is not None or not exclude_none)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #20)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict FAILED                  [  4%]

================================== FAILURES ===================================
______________________________ test_encode_dict _______________________________
tests\test_jsonable_encoder.py:78: in test_encode_dict
    assert jsonable_encoder(pet, include={"name"}) == {"name": "Firulais"}
E   AssertionError: assert {'name': 'Fir...name': 'Foo'}} == {'name': 'Firulais'}
E     
E     Omitting 1 identical items, use -vv to show
E     Left contains 1 more item:
E     {'owner': {'name': 'Foo'}}
E     
E     Full diff:
E       {...
E     
E
```
</details>

---

### Mutant #21

- **Operator:** LCR
- **Routine:** jsonable_encoder
- **Line:** 277
- **Status:** SURVIVED
- **Description:** Replace 'or' with 'and' at line 277

**Original Code:**
```python
and (value is not None or not exclude_none)
```

**Mutated Code:**
```python
and (value is not None and not exclude_none)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #21)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #22

- **Operator:** LCR
- **Routine:** jsonable_encoder
- **Line:** 278
- **Status:** KILLED
- **Description:** Replace 'and' with 'or' at line 278

**Original Code:**
```python
and key in allowed_keys
```

**Mutated Code:**
```python
or key in allowed_keys
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #22)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict FAILED                  [  4%]

================================== FAILURES ===================================
______________________________ test_encode_dict _______________________________
tests\test_jsonable_encoder.py:78: in test_encode_dict
    assert jsonable_encoder(pet, include={"name"}) == {"name": "Firulais"}
E   AssertionError: assert {'name': 'Fir...name': 'Foo'}} == {'name': 'Firulais'}
E     
E     Omitting 1 identical items, use -vv to show
E     Left contains 1 more item:
E     {'owner': {'name': 'Foo'}}
E     
E     Full diff:
E       {...
E     
E
```
</details>

---

### Mutant #23

- **Operator:** CDL
- **Routine:** decimal_encoder
- **Line:** 61
- **Status:** KILLED
- **Description:** Replace '0' with '1' at line 61

**Original Code:**
```python
if isinstance(exponent, int) and exponent >= 0:
```

**Mutated Code:**
```python
if isinstance(exponent, int) and exponent >= 1:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #23)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #24

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 128
- **Status:** KILLED
- **Description:** Replace 'None,' with '{},' at line 128

**Original Code:**
```python
] = None,
```

**Mutated Code:**
```python
] = {},
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #24)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict FAILED                  [  4%]

================================== FAILURES ===================================
______________________________ test_encode_dict _______________________________
tests\test_jsonable_encoder.py:77: in test_encode_dict
    assert jsonable_encoder(pet) == {"name": "Firulais", "owner": {"name": "Foo"}}
E   AssertionError: assert {} == {'name': 'Fir...name': 'Foo'}}
E     
E     Right contains 2 more items:
E     {'name': 'Firulais', 'owner': {'name': 'Foo'}}
E     
E     Full diff:
E     + {}
E     - {...
E     
E     ...Full output truncat
```
</details>

---

### Mutant #25

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 137
- **Status:** SURVIVED
- **Description:** Replace 'None,' with '{},' at line 137

**Original Code:**
```python
] = None,
```

**Mutated Code:**
```python
] = {},
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #25)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #26

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 149
- **Status:** KILLED
- **Description:** Replace '= True' with '= False' at line 149

**Original Code:**
```python
] = True,
```

**Mutated Code:**
```python
] = False,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #26)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #27

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 149
- **Status:** KILLED
- **Description:** Replace 'True,' with 'False,' at line 149

**Original Code:**
```python
] = True,
```

**Mutated Code:**
```python
] = False,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #27)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #28

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 159
- **Status:** KILLED
- **Description:** Replace '= False' with '= True' at line 159

**Original Code:**
```python
] = False,
```

**Mutated Code:**
```python
] = True,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #28)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #29

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 159
- **Status:** KILLED
- **Description:** Replace 'False,' with 'True,' at line 159

**Original Code:**
```python
] = False,
```

**Mutated Code:**
```python
] = True,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #29)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #30

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 169
- **Status:** KILLED
- **Description:** Replace '= False' with '= True' at line 169

**Original Code:**
```python
] = False,
```

**Mutated Code:**
```python
] = True,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #30)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #31

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 169
- **Status:** KILLED
- **Description:** Replace 'False,' with 'True,' at line 169

**Original Code:**
```python
] = False,
```

**Mutated Code:**
```python
] = True,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #31)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #32

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 178
- **Status:** SURVIVED
- **Description:** Replace '= False' with '= True' at line 178

**Original Code:**
```python
] = False,
```

**Mutated Code:**
```python
] = True,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #32)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #33

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 178
- **Status:** SURVIVED
- **Description:** Replace 'False,' with 'True,' at line 178

**Original Code:**
```python
] = False,
```

**Mutated Code:**
```python
] = True,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #33)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #34

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 187
- **Status:** SURVIVED
- **Description:** Replace 'None,' with '{},' at line 187

**Original Code:**
```python
] = None,
```

**Mutated Code:**
```python
] = {},
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #34)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #35

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 199
- **Status:** SURVIVED
- **Description:** Replace '= True' with '= False' at line 199

**Original Code:**
```python
] = True,
```

**Mutated Code:**
```python
] = False,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #35)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #36

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 199
- **Status:** SURVIVED
- **Description:** Replace 'True,' with 'False,' at line 199

**Original Code:**
```python
] = True,
```

**Mutated Code:**
```python
] = False,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #36)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict PASSED                  [  4%]
tests/test_jsonable_encoder.py::test_encode_dict_include_exclude_list PASSED [  8%]
tests/test_jsonable_encoder.py::test_encode_class PASSED                 [ 12%]
tests/test_jsonable_encoder.py::test_encode_dictable PASSED              [ 16%]
tests/test_jsonable_encoder.py::test_encode_dataclass PASSED             [ 20%]
tests/test_jsonable_encoder.py::test_encode_unsupported PASSED           [ 25%]
tests/test_jsonable_encoder.py::test_encode_custom_json_encoders_model_pydanticv2 PASSED [ 29%]
tests/test_jsonable_encoder.py::test_json
```
</details>

---

### Mutant #37

- **Operator:** CDL
- **Routine:** jsonable_encoder
- **Line:** 262
- **Status:** KILLED
- **Description:** Replace 'return None' with 'return {}' at line 262

**Original Code:**
```python
return None
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #37)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #38

- **Operator:** UOI
- **Routine:** decimal_encoder
- **Line:** 61
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 61

**Original Code:**
```python
if isinstance(exponent, int) and exponent >= 0:
```

**Mutated Code:**
```python
if not (isinstance(exponent, int) and exponent >= 0):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #38)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #39

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 214
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 214

**Original Code:**
```python
if custom_encoder:
```

**Mutated Code:**
```python
if not (custom_encoder):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #39)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #40

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 215
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 215

**Original Code:**
```python
if type(obj) in custom_encoder:
```

**Mutated Code:**
```python
if not (type(obj) in custom_encoder):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #40)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #41

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 219
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 219

**Original Code:**
```python
if isinstance(obj, encoder_type):
```

**Mutated Code:**
```python
if not (isinstance(obj, encoder_type)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #41)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #42

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 225
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 225

**Original Code:**
```python
if isinstance(obj, BaseModel):
```

**Mutated Code:**
```python
if not (isinstance(obj, BaseModel)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #42)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #43

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 241
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 241

**Original Code:**
```python
if dataclasses.is_dataclass(obj):
```

**Mutated Code:**
```python
if not (dataclasses.is_dataclass(obj)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #43)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #44

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 255
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 255

**Original Code:**
```python
if isinstance(obj, Enum):
```

**Mutated Code:**
```python
if not (isinstance(obj, Enum)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #44)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #45

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 257
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 257

**Original Code:**
```python
if isinstance(obj, PurePath):
```

**Mutated Code:**
```python
if not (isinstance(obj, PurePath)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #45)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #46

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 259
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 259

**Original Code:**
```python
if isinstance(obj, (str, int, float, type(None))):
```

**Mutated Code:**
```python
if not (isinstance(obj, (str, int, float, type(None)))):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #46)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #47

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 261
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 261

**Original Code:**
```python
if isinstance(obj, PydanticUndefinedType):
```

**Mutated Code:**
```python
if not (isinstance(obj, PydanticUndefinedType)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #47)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #48

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 263
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 263

**Original Code:**
```python
if isinstance(obj, dict):
```

**Mutated Code:**
```python
if not (isinstance(obj, dict)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #48)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #49

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 298
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 298

**Original Code:**
```python
if isinstance(obj, (list, set, frozenset, GeneratorType, tuple, deque)):
```

**Mutated Code:**
```python
if not (isinstance(obj, (list, set, frozenset, GeneratorType, tuple, deque))):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #49)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #50

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 316
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 316

**Original Code:**
```python
if type(obj) in ENCODERS_BY_TYPE:
```

**Mutated Code:**
```python
if not (type(obj) in ENCODERS_BY_TYPE):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #50)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #51

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 319
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 319

**Original Code:**
```python
if isinstance(obj, classes_tuple):
```

**Mutated Code:**
```python
if not (isinstance(obj, classes_tuple)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #51)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #52

- **Operator:** UOI
- **Routine:** jsonable_encoder
- **Line:** 321
- **Status:** KILLED
- **Description:** Insert 'not' operator in condition at line 321

**Original Code:**
```python
if is_pydantic_v1_model_instance(obj):
```

**Mutated Code:**
```python
if not (is_pydantic_v1_model_instance(obj)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #52)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #53

- **Operator:** RIL
- **Routine:** isoformat
- **Line:** 37
- **Status:** KILLED
- **Description:** Replace return value with None at line 37

**Original Code:**
```python
return o.isoformat()
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #53)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #54

- **Operator:** RIL
- **Routine:** isoformat
- **Line:** 37
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 37

**Original Code:**
```python
return o.isoformat()
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #54)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #55

- **Operator:** RIL
- **Routine:** isoformat
- **Line:** 37
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 37

**Original Code:**
```python
return o.isoformat()
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #55)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #56

- **Operator:** RIL
- **Routine:** decimal_encoder
- **Line:** 62
- **Status:** KILLED
- **Description:** Replace return value with None at line 62

**Original Code:**
```python
return int(dec_value)
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #56)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #57

- **Operator:** RIL
- **Routine:** decimal_encoder
- **Line:** 62
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 62

**Original Code:**
```python
return int(dec_value)
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #57)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #58

- **Operator:** RIL
- **Routine:** decimal_encoder
- **Line:** 62
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 62

**Original Code:**
```python
return int(dec_value)
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #58)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #59

- **Operator:** RIL
- **Routine:** decimal_encoder
- **Line:** 64
- **Status:** KILLED
- **Description:** Replace return value with None at line 64

**Original Code:**
```python
return float(dec_value)
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #59)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #60

- **Operator:** RIL
- **Routine:** decimal_encoder
- **Line:** 64
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 64

**Original Code:**
```python
return float(dec_value)
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #60)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #61

- **Operator:** RIL
- **Routine:** decimal_encoder
- **Line:** 64
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 64

**Original Code:**
```python
return float(dec_value)
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #61)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #62

- **Operator:** RIL
- **Routine:** generate_encoders_by_class_tuples
- **Line:** 105
- **Status:** KILLED
- **Description:** Replace return value with None at line 105

**Original Code:**
```python
return encoders_by_class_tuples
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #62)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #63

- **Operator:** RIL
- **Routine:** generate_encoders_by_class_tuples
- **Line:** 105
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 105

**Original Code:**
```python
return encoders_by_class_tuples
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #63)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #64

- **Operator:** RIL
- **Routine:** generate_encoders_by_class_tuples
- **Line:** 105
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 105

**Original Code:**
```python
return encoders_by_class_tuples
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #64)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #65

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 216
- **Status:** KILLED
- **Description:** Replace return value with None at line 216

**Original Code:**
```python
return custom_encoder[type(obj)](obj)
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #65)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #66

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 216
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 216

**Original Code:**
```python
return custom_encoder[type(obj)](obj)
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #66)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #67

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 216
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 216

**Original Code:**
```python
return custom_encoder[type(obj)](obj)
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #67)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #68

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 220
- **Status:** KILLED
- **Description:** Replace return value with None at line 220

**Original Code:**
```python
return encoder_instance(obj)
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #68)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #69

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 220
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 220

**Original Code:**
```python
return encoder_instance(obj)
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #69)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #70

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 220
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 220

**Original Code:**
```python
return encoder_instance(obj)
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #70)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #71

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 235
- **Status:** KILLED
- **Description:** Replace return value with None at line 235

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #71)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #72

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 235
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 235

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #72)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #73

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 235
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 235

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #73)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #74

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 244
- **Status:** KILLED
- **Description:** Replace return value with None at line 244

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #74)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #75

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 244
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 244

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #75)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #76

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 244
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 244

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #76)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #77

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 256
- **Status:** KILLED
- **Description:** Replace return value with None at line 256

**Original Code:**
```python
return obj.value
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #77)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #78

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 256
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 256

**Original Code:**
```python
return obj.value
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #78)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #79

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 256
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 256

**Original Code:**
```python
return obj.value
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #79)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #80

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 258
- **Status:** KILLED
- **Description:** Replace return value with None at line 258

**Original Code:**
```python
return str(obj)
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #80)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #81

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 258
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 258

**Original Code:**
```python
return str(obj)
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #81)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #82

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 258
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 258

**Original Code:**
```python
return str(obj)
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #82)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #83

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 260
- **Status:** KILLED
- **Description:** Replace return value with None at line 260

**Original Code:**
```python
return obj
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #83)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #84

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 260
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 260

**Original Code:**
```python
return obj
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #84)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #85

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 260
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 260

**Original Code:**
```python
return obj
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #85)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #86

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 297
- **Status:** KILLED
- **Description:** Replace return value with None at line 297

**Original Code:**
```python
return encoded_dict
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #86)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #87

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 297
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 297

**Original Code:**
```python
return encoded_dict
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #87)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #88

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 297
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 297

**Original Code:**
```python
return encoded_dict
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #88)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #89

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 314
- **Status:** KILLED
- **Description:** Replace return value with None at line 314

**Original Code:**
```python
return encoded_list
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #89)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #90

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 314
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 314

**Original Code:**
```python
return encoded_list
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #90)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #91

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 314
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 314

**Original Code:**
```python
return encoded_list
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #91)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #92

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 317
- **Status:** KILLED
- **Description:** Replace return value with None at line 317

**Original Code:**
```python
return ENCODERS_BY_TYPE[type(obj)](obj)
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #92)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #93

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 317
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 317

**Original Code:**
```python
return ENCODERS_BY_TYPE[type(obj)](obj)
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #93)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #94

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 317
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 317

**Original Code:**
```python
return ENCODERS_BY_TYPE[type(obj)](obj)
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #94)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #95

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 320
- **Status:** KILLED
- **Description:** Replace return value with None at line 320

**Original Code:**
```python
return encoder(obj)
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #95)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #96

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 320
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 320

**Original Code:**
```python
return encoder(obj)
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #96)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #97

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 320
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 320

**Original Code:**
```python
return encoder(obj)
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #97)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #98

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 336
- **Status:** KILLED
- **Description:** Replace return value with None at line 336

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return None
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #98)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #99

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 336
- **Status:** KILLED
- **Description:** Replace return value with empty dict at line 336

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return {}
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #99)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #100

- **Operator:** RIL
- **Routine:** jsonable_encoder
- **Line:** 336
- **Status:** KILLED
- **Description:** Replace return value with empty list at line 336

**Original Code:**
```python
return jsonable_encoder(
```

**Mutated Code:**
```python
return []
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #100)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #101

- **Operator:** MSI
- **Routine:** generate_encoders_by_class_tuples
- **Line:** 103
- **Status:** KILLED
- **Description:** Replace '.items()' with '.keys()' at line 103

**Original Code:**
```python
for type_, encoder in type_encoder_map.items():
```

**Mutated Code:**
```python
for type_, encoder in type_encoder_map.keys():
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #101)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #102

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 218
- **Status:** KILLED
- **Description:** Replace '.items()' with '.keys()' at line 218

**Original Code:**
```python
for encoder_type, encoder_instance in custom_encoder.items():
```

**Mutated Code:**
```python
for encoder_type, encoder_instance in custom_encoder.keys():
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #102)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #103

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 226
- **Status:** KILLED
- **Description:** Replace '.model_dump(' with '.model_dump_json(' at line 226

**Original Code:**
```python
obj_dict = obj.model_dump(
```

**Mutated Code:**
```python
obj_dict = obj.model_dump_json(
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #103)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #104

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 243
- **Status:** KILLED
- **Description:** Replace '.asdict(' with '.astuple(' at line 243

**Original Code:**
```python
obj_dict = dataclasses.asdict(obj)
```

**Mutated Code:**
```python
obj_dict = dataclasses.astuple(obj)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #104)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #105

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 265
- **Status:** KILLED
- **Description:** Replace '.keys()' with '.values()' at line 265

**Original Code:**
```python
allowed_keys = set(obj.keys())
```

**Mutated Code:**
```python
allowed_keys = set(obj.values())
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #105)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #106

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 270
- **Status:** KILLED
- **Description:** Replace '.items()' with '.keys()' at line 270

**Original Code:**
```python
for key, value in obj.items():
```

**Mutated Code:**
```python
for key, value in obj.keys():
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #106)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #107

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 301
- **Status:** KILLED
- **Description:** Replace '.append(' with '.insert(0, ' at line 301

**Original Code:**
```python
encoded_list.append(
```

**Mutated Code:**
```python
encoded_list.insert(0,
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #107)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #108

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 318
- **Status:** KILLED
- **Description:** Replace '.items()' with '.keys()' at line 318

**Original Code:**
```python
for encoder, classes_tuple in encoders_by_class_tuples.items():
```

**Mutated Code:**
```python
for encoder, classes_tuple in encoders_by_class_tuples.keys():
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #108)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #109

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 330
- **Status:** KILLED
- **Description:** Replace '.append(' with '.insert(0, ' at line 330

**Original Code:**
```python
errors.append(e)
```

**Mutated Code:**
```python
errors.insert(0, e)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #109)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #110

- **Operator:** MSI
- **Routine:** jsonable_encoder
- **Line:** 334
- **Status:** KILLED
- **Description:** Replace '.append(' with '.insert(0, ' at line 334

**Original Code:**
```python
errors.append(e)
```

**Mutated Code:**
```python
errors.insert(0, e)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #110)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #111

- **Operator:** IOD
- **Routine:** jsonable_encoder
- **Line:** 215
- **Status:** KILLED
- **Description:** Replace 'in' with 'not in' at line 215

**Original Code:**
```python
if type(obj) in custom_encoder:
```

**Mutated Code:**
```python
if type(obj) not in custom_encoder:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #111)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #112

- **Operator:** IOD
- **Routine:** jsonable_encoder
- **Line:** 278
- **Status:** KILLED
- **Description:** Replace 'in' with 'not in' at line 278

**Original Code:**
```python
and key in allowed_keys
```

**Mutated Code:**
```python
and key not in allowed_keys
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #112)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 24 items

tests/test_jsonable_encoder.py::test_encode_dict FAILED                  [  4%]

================================== FAILURES ===================================
______________________________ test_encode_dict _______________________________
tests\test_jsonable_encoder.py:77: in test_encode_dict
    assert jsonable_encoder(pet) == {"name": "Firulais", "owner": {"name": "Foo"}}
E   AssertionError: assert {} == {'name': 'Fir...name': 'Foo'}}
E     
E     Right contains 2 more items:
E     {'name': 'Firulais', 'owner': {'name': 'Foo'}}
E     
E     Full diff:
E     + {}
E     - {...
E     
E     ...Full output truncat
```
</details>

---

### Mutant #113

- **Operator:** IOD
- **Routine:** jsonable_encoder
- **Line:** 316
- **Status:** KILLED
- **Description:** Replace 'in' with 'not in' at line 316

**Original Code:**
```python
if type(obj) in ENCODERS_BY_TYPE:
```

**Mutated Code:**
```python
if type(obj) not in ENCODERS_BY_TYPE:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #113)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #114

- **Operator:** TYP
- **Routine:** decimal_encoder
- **Line:** 61
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 61

**Original Code:**
```python
if isinstance(exponent, int) and exponent >= 0:
```

**Mutated Code:**
```python
if not isinstance(exponent, int) and exponent >= 0:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #114)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #115

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 215
- **Status:** KILLED
- **Description:** Negate type check 'type(' at line 215

**Original Code:**
```python
if type(obj) in custom_encoder:
```

**Mutated Code:**
```python
if str(type(obj) in custom_encoder:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #115)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #116

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 216
- **Status:** KILLED
- **Description:** Negate type check 'type(' at line 216

**Original Code:**
```python
return custom_encoder[type(obj)](obj)
```

**Mutated Code:**
```python
return custom_encoder[str(type(obj)](obj)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #116)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #117

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 219
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 219

**Original Code:**
```python
if isinstance(obj, encoder_type):
```

**Mutated Code:**
```python
if not isinstance(obj, encoder_type):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #117)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #118

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 225
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 225

**Original Code:**
```python
if isinstance(obj, BaseModel):
```

**Mutated Code:**
```python
if not isinstance(obj, BaseModel):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #118)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #119

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 241
- **Status:** KILLED
- **Description:** Negate type check 'is_dataclass(' at line 241

**Original Code:**
```python
if dataclasses.is_dataclass(obj):
```

**Mutated Code:**
```python
if dataclasses.not is_dataclass(obj):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #119)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #120

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 255
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 255

**Original Code:**
```python
if isinstance(obj, Enum):
```

**Mutated Code:**
```python
if not isinstance(obj, Enum):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #120)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #121

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 257
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 257

**Original Code:**
```python
if isinstance(obj, PurePath):
```

**Mutated Code:**
```python
if not isinstance(obj, PurePath):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #121)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #122

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 259
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 259

**Original Code:**
```python
if isinstance(obj, (str, int, float, type(None))):
```

**Mutated Code:**
```python
if not isinstance(obj, (str, int, float, type(None))):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #122)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #123

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 259
- **Status:** KILLED
- **Description:** Negate type check 'type(' at line 259

**Original Code:**
```python
if isinstance(obj, (str, int, float, type(None))):
```

**Mutated Code:**
```python
if isinstance(obj, (str, int, float, str(type(None))):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #123)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #124

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 261
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 261

**Original Code:**
```python
if isinstance(obj, PydanticUndefinedType):
```

**Mutated Code:**
```python
if not isinstance(obj, PydanticUndefinedType):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #124)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #125

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 263
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 263

**Original Code:**
```python
if isinstance(obj, dict):
```

**Mutated Code:**
```python
if not isinstance(obj, dict):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #125)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #126

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 298
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 298

**Original Code:**
```python
if isinstance(obj, (list, set, frozenset, GeneratorType, tuple, deque)):
```

**Mutated Code:**
```python
if not isinstance(obj, (list, set, frozenset, GeneratorType, tuple, deque)):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #126)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #127

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 316
- **Status:** KILLED
- **Description:** Negate type check 'type(' at line 316

**Original Code:**
```python
if type(obj) in ENCODERS_BY_TYPE:
```

**Mutated Code:**
```python
if str(type(obj) in ENCODERS_BY_TYPE:
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #127)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #128

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 317
- **Status:** KILLED
- **Description:** Negate type check 'type(' at line 317

**Original Code:**
```python
return ENCODERS_BY_TYPE[type(obj)](obj)
```

**Mutated Code:**
```python
return ENCODERS_BY_TYPE[str(type(obj)](obj)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #128)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #129

- **Operator:** TYP
- **Routine:** jsonable_encoder
- **Line:** 319
- **Status:** KILLED
- **Description:** Negate type check 'isinstance(' at line 319

**Original Code:**
```python
if isinstance(obj, classes_tuple):
```

**Mutated Code:**
```python
if not isinstance(obj, classes_tuple):
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #129)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #130

- **Operator:** DCI
- **Routine:** jsonable_encoder
- **Line:** 267
- **Status:** KILLED
- **Description:** Replace '&=' with '|=' at line 267

**Original Code:**
```python
allowed_keys &= set(include)
```

**Mutated Code:**
```python
allowed_keys |= set(include)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #130)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #131

- **Operator:** DCI
- **Routine:** jsonable_encoder
- **Line:** 269
- **Status:** KILLED
- **Description:** Replace '-=' with '+=' at line 269

**Original Code:**
```python
allowed_keys -= set(exclude)
```

**Mutated Code:**
```python
allowed_keys += set(exclude)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #131)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #132

- **Operator:** FCR
- **Routine:** decimal_encoder
- **Line:** 60
- **Status:** KILLED
- **Description:** Replace 'tuple(' with 'list(' at line 60

**Original Code:**
```python
exponent = dec_value.as_tuple().exponent
```

**Mutated Code:**
```python
exponent = dec_value.as_list().exponent
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #132)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #133

- **Operator:** FCR
- **Routine:** decimal_encoder
- **Line:** 62
- **Status:** KILLED
- **Description:** Replace 'int(' with 'float(' at line 62

**Original Code:**
```python
return int(dec_value)
```

**Mutated Code:**
```python
return float(dec_value)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #133)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #134

- **Operator:** FCR
- **Routine:** decimal_encoder
- **Line:** 64
- **Status:** KILLED
- **Description:** Replace 'float(' with 'int(' at line 64

**Original Code:**
```python
return float(dec_value)
```

**Mutated Code:**
```python
return int(dec_value)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #134)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #135

- **Operator:** FCR
- **Routine:** generate_encoders_by_class_tuples
- **Line:** 100
- **Status:** KILLED
- **Description:** Replace 'dict(' with 'list(' at line 100

**Original Code:**
```python
encoders_by_class_tuples: dict[Callable[[Any], Any], tuple[Any, ...]] = defaultdict(
```

**Mutated Code:**
```python
encoders_by_class_tuples: dict[Callable[[Any], Any], tuple[Any, ...]] = defaultlist(
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #135)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #136

- **Operator:** FCR
- **Routine:** jsonable_encoder
- **Line:** 222
- **Status:** KILLED
- **Description:** Replace 'set(' with 'frozenset(' at line 222

**Original Code:**
```python
include = set(include)
```

**Mutated Code:**
```python
include = frozenset(include)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #136)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #137

- **Operator:** FCR
- **Routine:** jsonable_encoder
- **Line:** 224
- **Status:** KILLED
- **Description:** Replace 'set(' with 'frozenset(' at line 224

**Original Code:**
```python
exclude = set(exclude)
```

**Mutated Code:**
```python
exclude = frozenset(exclude)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #137)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #138

- **Operator:** FCR
- **Routine:** jsonable_encoder
- **Line:** 243
- **Status:** KILLED
- **Description:** Replace 'dict(' with 'list(' at line 243

**Original Code:**
```python
obj_dict = dataclasses.asdict(obj)
```

**Mutated Code:**
```python
obj_dict = dataclasses.aslist(obj)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #138)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #139

- **Operator:** FCR
- **Routine:** jsonable_encoder
- **Line:** 258
- **Status:** KILLED
- **Description:** Replace 'str(' with 'repr(' at line 258

**Original Code:**
```python
return str(obj)
```

**Mutated Code:**
```python
return repr(obj)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #139)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #140

- **Operator:** FCR
- **Routine:** jsonable_encoder
- **Line:** 265
- **Status:** KILLED
- **Description:** Replace 'set(' with 'frozenset(' at line 265

**Original Code:**
```python
allowed_keys = set(obj.keys())
```

**Mutated Code:**
```python
allowed_keys = frozenset(obj.keys())
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #140)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #141

- **Operator:** FCR
- **Routine:** jsonable_encoder
- **Line:** 267
- **Status:** KILLED
- **Description:** Replace 'set(' with 'frozenset(' at line 267

**Original Code:**
```python
allowed_keys &= set(include)
```

**Mutated Code:**
```python
allowed_keys &= frozenset(include)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #141)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #142

- **Operator:** FCR
- **Routine:** jsonable_encoder
- **Line:** 269
- **Status:** KILLED
- **Description:** Replace 'set(' with 'frozenset(' at line 269

**Original Code:**
```python
allowed_keys -= set(exclude)
```

**Mutated Code:**
```python
allowed_keys -= frozenset(exclude)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #142)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

### Mutant #143

- **Operator:** FCR
- **Routine:** jsonable_encoder
- **Line:** 327
- **Status:** KILLED
- **Description:** Replace 'dict(' with 'list(' at line 327

**Original Code:**
```python
data = dict(obj)
```

**Mutated Code:**
```python
data = list(obj)
```

**Unified Diff:** See `consolidated_mutations.diff` (Mutant #143)

<details>
<summary>Test Output</summary>

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\eulun\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\eulun\Desktop\473\fastapi-mutation-testing-2
configfile: pyproject.toml
plugins: anyio-4.6.0
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_jsonable_encoder.py _______________
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\python.py:507: in importtestmodule
    mod = import_path(
..\..\..\AppData\Local\Programs\Python\Python312\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^
```
</details>

---

