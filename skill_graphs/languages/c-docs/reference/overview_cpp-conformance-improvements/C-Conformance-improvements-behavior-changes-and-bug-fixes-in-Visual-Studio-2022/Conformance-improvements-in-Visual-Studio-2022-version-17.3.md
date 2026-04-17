##  Conformance improvements in Visual Studio 2022 version 17.3
Visual Studio 2022 version 17.3 contains the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#c-improved-modifier-compatibility-checking-between-pointers)
### C: Improved modifier compatibility checking between pointers
The C compiler didn't properly compare modifiers between pointers, especially `void*`. This defect could result in an improper diagnosis of incompatibility between `const int**` and `void*` and compatibility between `int* volatile*` and `void*`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-2)
#### Example
C
Copy
```
void fn(void* pv) { (pv); }

int main()
{
    int t = 42;
    int* pt = &t;
    int* volatile * i = &pt;
    fn(i);    // Now raises C4090
    const int** j = &pt;
    fn(j);    // No longer raises C4090
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_172)
