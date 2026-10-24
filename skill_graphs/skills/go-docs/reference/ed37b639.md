# Frequently Asked Questions (FAQ)
Table of Contents
---

[Origins](https://go.dev/doc/faq#Origins)
    [What is the purpose of the project?](https://go.dev/doc/faq#What_is_the_purpose_of_the_project)     [What is the history of the project?](https://go.dev/doc/faq#history)     [What’s the origin of the gopher mascot?](https://go.dev/doc/faq#gopher)     [Is the language called Go or Golang?](https://go.dev/doc/faq#go_or_golang)     [Why did you create a new language?](https://go.dev/doc/faq#creating_a_new_language)     [What are Go’s ancestors?](https://go.dev/doc/faq#ancestors)     [What are the guiding principles in the design?](https://go.dev/doc/faq#principles)

[Usage](https://go.dev/doc/faq#Usage)
    [Is Google using Go internally?](https://go.dev/doc/faq#internal_usage)     [What other companies use Go?](https://go.dev/doc/faq#external_usage)     [Do Go programs link with C/C++ programs?](https://go.dev/doc/faq#Do_Go_programs_link_with_Cpp_programs)     [What IDEs does Go support?](https://go.dev/doc/faq#ide)     [Does Go support Google’s protocol buffers?](https://go.dev/doc/faq#protocol_buffers)

[Design](https://go.dev/doc/faq#Design)
    [Does Go have a runtime?](https://go.dev/doc/faq#runtime)     [What’s up with Unicode identifiers?](https://go.dev/doc/faq#unicode_identifiers)     [Why does Go not have feature X?](https://go.dev/doc/faq#Why_doesnt_Go_have_feature_X)     [When did Go get generic types?](https://go.dev/doc/faq#generics)     [Why was Go initially released without generic types?](https://go.dev/doc/faq#beginning_generics)     [Why does Go not have exceptions?](https://go.dev/doc/faq#exceptions)     [Why does Go not have assertions?](https://go.dev/doc/faq#assertions)     [Why build concurrency on the ideas of CSP?](https://go.dev/doc/faq#csp)     [Why goroutines instead of threads?](https://go.dev/doc/faq#goroutines)     [Why are map operations not defined to be atomic?](https://go.dev/doc/faq#atomic_maps)     [Will you accept my language change?](https://go.dev/doc/faq#language_changes)

[Types](https://go.dev/doc/faq#types)
    [Is Go an object-oriented language?](https://go.dev/doc/faq#Is_Go_an_object-oriented_language)     [How do I get dynamic dispatch of methods?](https://go.dev/doc/faq#How_do_I_get_dynamic_dispatch_of_methods)     [Why is there no type inheritance?](https://go.dev/doc/faq#inheritance)     [Why is len a function and not a method?](https://go.dev/doc/faq#methods_on_basics)     [Why does Go not support overloading of methods and operators?](https://go.dev/doc/faq#overloading)     [Why doesn’t Go have “implements” declarations?](https://go.dev/doc/faq#implements_interface)     [How can I guarantee my type satisfies an interface?](https://go.dev/doc/faq#guarantee_satisfies_interface)     [Why doesn’t type T satisfy the Equal interface?](https://go.dev/doc/faq#t_and_equal_interface)     [Can I convert a []T to an []interface{}?](https://go.dev/doc/faq#convert_slice_of_interface)     [Can I convert []T1 to []T2 if T1 and T2 have the same underlying type?](https://go.dev/doc/faq#convert_slice_with_same_underlying_type)     [Why is my nil error value not equal to nil?](https://go.dev/doc/faq#nil_error)     [Why do zero-size types behave oddly?](https://go.dev/doc/faq#zero_size_types)     [Why are there no untagged unions, as in C?](https://go.dev/doc/faq#unions)     [Why does Go not have variant types?](https://go.dev/doc/faq#variant_types)     [Why does Go not have covariant result types?](https://go.dev/doc/faq#covariant_types)

[Values](https://go.dev/doc/faq#Values)
    [Why does Go not provide implicit numeric conversions?](https://go.dev/doc/faq#conversions)     [How do constants work in Go?](https://go.dev/doc/faq#constants)     [Why are maps built in?](https://go.dev/doc/faq#builtin_maps)     [Why don’t maps allow slices as keys?](https://go.dev/doc/faq#map_keys)     [Why are maps, slices, and channels references while arrays are values?](https://go.dev/doc/faq#references)

[Writing Code](https://go.dev/doc/faq#Writing_Code)
    [How are libraries documented?](https://go.dev/doc/faq#How_are_libraries_documented)     [Is there a Go programming style guide?](https://go.dev/doc/faq#Is_there_a_Go_programming_style_guide)     [How do I submit patches to the Go libraries?](https://go.dev/doc/faq#How_do_I_submit_patches_to_the_Go_libraries)     [Why does “go get” use HTTPS when cloning a repository?](https://go.dev/doc/faq#git_https)     [How should I manage package versions using “go get”?](https://go.dev/doc/faq#get_version) |

[Pointers and Allocation](https://go.dev/doc/faq#Pointers)
    [When are function parameters passed by value?](https://go.dev/doc/faq#pass_by_value)     [When should I use a pointer to an interface?](https://go.dev/doc/faq#pointer_to_interface)     [Should I define methods on values or pointers?](https://go.dev/doc/faq#methods_on_values_or_pointers)     [What’s the difference between new and make?](https://go.dev/doc/faq#new_and_make)     [What is the size of an int on a 64 bit machine?](https://go.dev/doc/faq#q_int_sizes)     [How do I know whether a variable is allocated on the heap or the stack?](https://go.dev/doc/faq#stack_or_heap)     [Why does my Go process use so much virtual memory?](https://go.dev/doc/faq#Why_does_my_Go_process_use_so_much_virtual_memory)

[Concurrency](https://go.dev/doc/faq#Concurrency)
    [What operations are atomic? What about mutexes?](https://go.dev/doc/faq#What_operations_are_atomic_What_about_mutexes)     [Why doesn’t my program run faster with more CPUs?](https://go.dev/doc/faq#parallel_slow)     [How can I control the number of CPUs?](https://go.dev/doc/faq#number_cpus)     [Why is there no goroutine ID?](https://go.dev/doc/faq#no_goroutine_id)

[Functions and Methods](https://go.dev/doc/faq#Functions_methods)
    [Why do T and *T have different method sets?](https://go.dev/doc/faq#different_method_sets)     [What happens with closures running as goroutines?](https://go.dev/doc/faq#closures_and_goroutines)

[Control Flow](https://go.dev/doc/faq#Control_flow)
    [Why does Go not have the ?: operator?](https://go.dev/doc/faq#Does_Go_have_a_ternary_form)

[Type Parameters](https://go.dev/doc/faq#Type_Parameters)
    [Why does Go have type parameters?](https://go.dev/doc/faq#why_generics)     [How are generics implemented in Go?](https://go.dev/doc/faq#generics_implementation)     [How do generics in Go compare to generics in other languages?](https://go.dev/doc/faq#generics_comparison)     [Why does Go use square brackets for type parameter lists?](https://go.dev/doc/faq#generic_brackets)     [Why does Go not support methods with type parameters?](https://go.dev/doc/faq#generic_methods)     [Why can’t I use a more specific type for the receiver of a parameterized type?](https://go.dev/doc/faq#types_in_method_declaration)     [Why can’t the compiler infer the type argument in my program?](https://go.dev/doc/faq#type_inference)

[Packages and Testing](https://go.dev/doc/faq#Packages_Testing)
    [How do I create a multifile package?](https://go.dev/doc/faq#How_do_I_create_a_multifile_package)     [How do I write a unit test?](https://go.dev/doc/faq#How_do_I_write_a_unit_test)     [Where is my favorite helper function for testing?](https://go.dev/doc/faq#testing_framework)     [Why isn’t X in the standard library?](https://go.dev/doc/faq#x_in_std)

[Implementation](https://go.dev/doc/faq#Implementation)
    [What compiler technology is used to build the compilers?](https://go.dev/doc/faq#What_compiler_technology_is_used_to_build_the_compilers)     [How is the run-time support implemented?](https://go.dev/doc/faq#How_is_the_run_time_support_implemented)     [Why is my trivial program such a large binary?](https://go.dev/doc/faq#Why_is_my_trivial_program_such_a_large_binary)     [Can I stop these complaints about my unused variable/import?](https://go.dev/doc/faq#unused_variables_and_imports)     [Why does my virus-scanning software think my Go distribution or compiled binary is infected?](https://go.dev/doc/faq#virus)

[Performance](https://go.dev/doc/faq#Performance)
    [Why does Go perform badly on benchmark X?](https://go.dev/doc/faq#Why_does_Go_perform_badly_on_benchmark_x)

[Changes from C](https://go.dev/doc/faq#change_from_c)
    [Why is the syntax so different from C?](https://go.dev/doc/faq#different_syntax)     [Why are declarations backwards?](https://go.dev/doc/faq#declarations_backwards)     [Why is there no pointer arithmetic?](https://go.dev/doc/faq#no_pointer_arithmetic)     [Why are ++ and -- statements and not expressions? And why postfix, not prefix?](https://go.dev/doc/faq#inc_dec)     [Why are there braces but no semicolons? And why can’t I put the opening brace on the next line? ](https://go.dev/doc/faq#semicolons)     [Why do garbage collection? Won’t it be too expensive?](https://go.dev/doc/faq#garbage_collection)
