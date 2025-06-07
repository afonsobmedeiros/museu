import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import { Login } from "./pages/login"
import { PrivateRoute } from './routes/PrivateRoute';
import { Dashboard } from './pages/dashboard';
import { Exibicoes } from './pages/exibicoes';
import { Colecoes } from './pages/colecoes';
import { Pecas } from './pages/pecas';
import { Curadores } from './pages/curadores';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />
        <Route
          path="/exhibitions"
          element={
            <PrivateRoute>
              <Exibicoes />
            </PrivateRoute>
          }
        />
        <Route
          path="/collections"
          element={
            <PrivateRoute>
              <Colecoes />
            </PrivateRoute>
          }
        />
        <Route
          path="/pieces"
          element={
            <PrivateRoute>
              <Pecas />
            </PrivateRoute>
          }
        />
        <Route
          path="/curators"
          element={
            <PrivateRoute>
              <Curadores />
            </PrivateRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
