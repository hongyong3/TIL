##### firebaseservice.js

```
getWeekMenus() {
	const weekmenusCollection = firestore.collection('weeklymenus')
	return weekmenusCollection
		.orderBy('week', 'desc')
		.get()
		.then((docSnapshots) => {
			return docSnapshots.docs.map((doc) => {
				let data = doc.data()
				return data
			})
		})
},
postWeekMenus(date, korean, star, special) {
	return firestore.collection(WEEKLYMENUS).add({
		date,
		korean,
		star,
		special
	})
}
```





```
postWeekMenu(date, korean, star, special) {
	return firestore.collection('weeklymenus').add({
		date,
		korean,
		star,
		special,
		uploadUser: store.user.email
	})
	.then(function(doRef) {
		firestore.collection('weeklymenus').doc(doRef.id).update({
			id: docRef.id
		})
		location.href="/weeklymenu"
	})
}
```



postWeekMenu(date, korean, star, special)

```
postWeekMenu(date, korean, star, special) {
          return firestore.collection('weeklymenus').add({
            date,
            korean,
            star,
            special,
          })
          .then(function(doRef) {
            firestore.collection('weeklymenus').doc(doRef.id).update({
              id: dcRef.id
            })
            location.href="/weeklymenu"
          })
        },
```



```
        postWeekMenus(date, korean, star, special) {
      		return firestore.collection('weeklymenus').add({
      			date,
      			korean,
      			star,
      			special
      		})
          console.log(this.menudata.menus[0]["korean"])
        },
```



```
        getWeeklyMenus.forEach(function(obj)) {
      		db.collection("weeklymenus").add({
      			id: obj.id,
      			date: obj.date,
      			korean: obj.korean,
      			star: obj.star,
      			special: obj.special
      		}).then(function(docRef) {
      				console.log("Document written with ID: ", docRef.id);
      		})
      		.catch(function(error) {
      			console.log("Error adding document: ", error);
      		})
      	}
```

