



 2    'products' => [




 3        ['name' => 'Desk 1', 'price' => 100],




 4        ['name' => 'Desk 2', 'price' => 150],




 5    ],




 6];




 7 



 8data_forget($data, 'products.*.price');




 9 



10/*




11    [




12        'products' => [




13            ['name' => 'Desk 1'],




14            ['name' => 'Desk 2'],




15        ],




16    ]




17*/




$data = [
    'products' => [
        ['name' => 'Desk 1', 'price' => 100],
        ['name' => 'Desk 2', 'price' => 150],
    ],
];

data_forget($data, 'products.*.price');

/*
    [
        'products' => [
            ['name' => 'Desk 1'],
            ['name' => 'Desk 2'],
        ],
    ]
*/

```

#### [`head()`](https://laravel.com/docs/12.x/helpers#method-head)
The `head` function returns the first element in the given array. If the array is empty, `false` will be returned:
```


1$array = [100, 200, 300];




2 



3$first = head($array);




4 



5// 100




$array = [100, 200, 300];

$first = head($array);

// 100

```

#### [`last()`](https://laravel.com/docs/12.x/helpers#method-last)
The `last` function returns the last element in the given array. If the array is empty, `false` will be returned:
```


1$array = [100, 200, 300];




2 



3$last = last($array);




4 



5// 300




$array = [100, 200, 300];

$last = last($array);

// 300

```
