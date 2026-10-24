# Write the images to a folder
dataset_iter = iter(dataset)
os.makedirs(IMAGE_FOLDER, exist_ok=True)
for i in range(N_IMAGES):
    image = next(dataset_iter)['image']
    image.save(f"images/{i}.jpg")

multimodal_cohere_ef = CohereEmbeddingFunction(
    model_name="embed-english-v3.0",
    api_key="YOUR_API_KEY",
)
image_loader = ImageLoader()

multimodal_collection = client.create_collection(
    name="multimodal",
    embedding_function=multimodal_cohere_ef,
    data_loader=image_loader)

image_uris = sorted([os.path.join(IMAGE_FOLDER, image_name) for image_name in os.listdir(IMAGE_FOLDER)])
ids = [str(i) for i in range(len(image_uris))]
for i in range(len(image_uris)):
    # max images per add is 1, see cohere docs https://docs.cohere.com/v2/reference/embed#request.body.images
    multimodal_collection.add(ids=[str(i)], uris=[image_uris[i]])

retrieved = multimodal_collection.query(query_texts=["animals"], include=['data'], n_results=3)

```
