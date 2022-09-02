import {useState} from 'react'
import './App.css';
import items  from './data';
import Menu from './menu'
import Categories from './cate'

function App() {
  const [menuItems, setMenuItems] = useState(items);
  const [categories, setCategories]= useState([]);

  const filterItems= (category)=>{
    const newItems= items.filter((item)=>{
      if(item.category===category){
        
      }
    })
  }
  return (
    <main>
      <section className='menu-section'>
        <div className="title">
          <h2>Our Menu</h2>
          <div className="underline"></div>
        </div>
        <Categories />
        <Menu items={menuItems}/>
        </section>
        
    </main>
  );
}

export default App;
