# Define K-means model
kmeans_model = KMeans(init='k-means++',  max_iter=400, random_state=42)


# Train the model
kmeans_model.fit(customersdata[['products_purchased','complains',
'money_spent']])
