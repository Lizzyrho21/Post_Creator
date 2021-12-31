
import './App.css';
import axios from 'axios';
import Posts from './components/Posts';
import { useState, useEffect } from "react"


function App() {
  const [posts, setPosts] = useState('');

  const url = 'http://localhost:8000/';


  useEffect(() => {
    getAllPosts();
  }, []);

  const getAllPosts = () => {
      
    axios.get(`${url}api/posts/`)
    .then(res => {
    let data = res.data;
    setPosts(data);
    console.log(posts);
    
      }).catch (err => {})


  }


  

  return (
    <div className="App">
      <h1>Forms with React!</h1>
      <Posts posts={posts} />
    </div>
  );
}


export default App;
