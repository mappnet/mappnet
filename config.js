// Конфигурация Firebase (замените на свои данные!)
const firebaseConfig = {
    apiKey: "ВАШ_API_KEY",
    authDomain: "ВАШ_PROJECT.firebaseapp.com",
    projectId: "ВАШ_PROJECT",
  };
  
  // Инициализация Firebase
  firebase.initializeApp(firebaseConfig);
  const db = firebase.firestore();