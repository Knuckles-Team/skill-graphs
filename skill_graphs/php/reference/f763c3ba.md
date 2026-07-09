## [Reranking](https://laravel.com/docs/12.x/ai-sdk#reranking)
Reranking allows you to reorder a list of documents based on their relevance to a given query. This is useful for improving search results by using semantic understanding:
The `Laravel\Ai\Reranking` class may be used to rerank documents:
```


 1use Laravel\Ai\Reranking;




 2 



 3$response = Reranking::of([




 4    'Django is a Python web framework.',




 5    'Laravel is a PHP web application framework.',




 6    'React is a JavaScript library for building user interfaces.',




 7])->rerank('PHP frameworks');




 8 



 9// Access the top result...




10$response->first()->document; // "Laravel is a PHP web application framework."




11$response->first()->score;    // 0.95




12$response->first()->index;    // 1 (original position)




use Laravel\Ai\Reranking;

$response = Reranking::of([
    'Django is a Python web framework.',
    'Laravel is a PHP web application framework.',
    'React is a JavaScript library for building user interfaces.',
])->rerank('PHP frameworks');

// Access the top result...
$response->first()->document; // "Laravel is a PHP web application framework."
$response->first()->score;    // 0.95
$response->first()->index;    // 1 (original position)

```

The `limit` method may be used to restrict the number of results returned:
```


1$response = Reranking::of($documents)




2    ->limit(5)




3    ->rerank('search query');




$response = Reranking::of($documents)
    ->limit(5)
    ->rerank('search query');

```

### [Reranking Collections](https://laravel.com/docs/12.x/ai-sdk#reranking-collections)
For convenience, Laravel collections may be reranked using the `rerank` macro. The first argument specifies which field(s) to use for reranking, and the second argument is the query:
```


 1// Rerank by a single field...




 2$posts = Post::all()




 3    ->rerank('body', 'Laravel tutorials');




 4 



 5// Rerank by multiple fields (sent as JSON)...




 6$reranked = $posts->rerank(['title', 'body'], 'Laravel tutorials');




 7 



 8// Rerank using a closure to build the document...




 9$reranked = $posts->rerank(




10    fn ($post) => $post->title.': '.$post->body,




11    'Laravel tutorials'




12);




// Rerank by a single field...
$posts = Post::all()
    ->rerank('body', 'Laravel tutorials');

// Rerank by multiple fields (sent as JSON)...
$reranked = $posts->rerank(['title', 'body'], 'Laravel tutorials');

// Rerank using a closure to build the document...
$reranked = $posts->rerank(
    fn ($post) => $post->title.': '.$post->body,
    'Laravel tutorials'
);

```

You may also limit the number of results and specify a provider:
```


1$reranked = $posts->rerank(




2    by: 'content',




3    query: 'Laravel tutorials',




4    limit: 10,




5    provider: Lab::Cohere




6);




$reranked = $posts->rerank(
    by: 'content',
    query: 'Laravel tutorials',
    limit: 10,
    provider: Lab::Cohere
);

```
