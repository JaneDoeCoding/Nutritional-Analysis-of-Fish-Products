import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css'; 

const container = document.getElementById('root');

if (container) {
  const root = ReactDOM.createRoot(container);
  root.render(
    <React.StrictMode>
      {/* Renders the main App component within StrictMode for development checks */}
      <App /> 
    </React.StrictMode>
  );
}
