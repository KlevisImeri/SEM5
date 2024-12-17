EF
- List the buyer pairs that have locations in the same city. A pair should be listed only once. EF
- Create a new category called _Expensive toys_ and reclassify here all the products whose price is greater than HUF 8,000!
Mongo
- Create a new category named _Expensive toys_ and move all products here that cost more than 8000!
``` c#
//3.2
Console.WriteLine("\t3.2:");
var catExpensiveToys = categoriesCollection.FindOneAndUpdate<Category>(
    filter: c => c.Name == "Expensive toys",
    update: Builders<Category>.Update.SetOnInsert(c => c.Name, "Expensive toys"),
    options: new FindOneAndUpdateOptions<Category, Category> { IsUpsert = true, ReturnDocument = ReturnDocument.After });

productsCollection.UpdateMany(
    filter: p => p.Price > 8000,
    update: Builders<Product>.Update.Set(p => p.CategoryID, catExpensiveToys.ID));
```

