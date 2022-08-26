import './App.css';

function App(props) {
  return (
    <div>
      <h1>{props.site}</h1>
      <a href={props.url}>こちら</a>
      <h2>楽しめましたか</h2>
    </div>
    
  );
}


export default App;