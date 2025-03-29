document.addEventListener('DOMContentLoaded', async () => {
    // Загружаем карты из Firebase
    const mapsRef = db.collection('maps');
    const snapshot = await mapsRef.limit(10).get(); // Первые 10 карт
  
    // Отображаем карточки
    const cardsList = document.getElementById('cards-list');
    snapshot.forEach(doc => {
      const map = doc.data();
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <h3>${map.title}</h3>
        <p>Тип: ${map.type}</p>
        <p>Год: ${map.year}</p>
        <img src="${map.thumbnailUrl}" alt="${map.title}" width="100%">
        <a href="${map.fileUrl}" target="_blank">Открыть карту</a>
      `;
      cardsList.appendChild(card);
    });
  
    // Поиск по тегам
    document.getElementById('search-btn').addEventListener('click', async () => {
      const query = document.getElementById('search-input').value;
      const filtered = await mapsRef.where('tags', 'array-contains', query).get();
      cardsList.innerHTML = '';
      filtered.forEach(doc => { /* ...аналогично... */ });
    });
  });