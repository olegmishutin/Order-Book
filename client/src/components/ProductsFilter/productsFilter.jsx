import './productsFilter.css'

export default function ProductsFilter(props) {
    return (
        <>
            <form className="products__filters">
                <div className="products__filters__filter">
                    <label htmlFor='min_price'>От</label>
                    <input type='number' name='min_price' id='min_price' placeholder='Минимальная цена'/>
                    <label htmlFor='max_price'>До</label>
                    <input type='number' name='max_price' id='max_price' placeholder='Максимальная цена'/>
                </div>
                <ul>
                    <li className="products__filters__filter">
                        <input type='checkbox' name='new_products' id='new_products'/>
                        <label htmlFor='new_products'>Сначала новые продукты</label>
                    </li>
                    <li className="products__filters__filter">
                        <input type='checkbox' name='old_products' id='old_products'/>
                        <label htmlFor='old_products'>Сначала старые продукты</label>
                    </li>
                    <li className="products__filters__filter">
                        <input type='checkbox' name='expensive_products' id='expensive_products'/>
                        <label htmlFor='expensive_products'>Сначала дорогие продукты</label>
                    </li>
                    <li className="products__filters__filter">
                        <input type='checkbox' name='cheap_products' id='cheap_products'/>
                        <label htmlFor='cheap_products'>Сначала дешёвые продукты</label>
                    </li>
                </ul>
                <button type='button' onClick={props.filterFunc}>Фильтровать</button>
            </form>
        </>
    )
}