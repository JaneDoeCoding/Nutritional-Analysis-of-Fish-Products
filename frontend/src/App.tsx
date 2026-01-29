// src/App.tsx
import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ProductDetail from './components/ProductDetail';
import ComparisonView from './components/ComparisonView';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        {/* Root route renders the landing page */}
        <Route path="/" element={<HomePage />} />

        {/* Individual product details page */}
        <Route path="/products/:id" element={<ProductDetail />} />

        {/* Side-by-side product comparison page */}
        <Route path="/compare" element={<ComparisonView />} />
      </Routes>
    </Router>
  );
};

export default App;
