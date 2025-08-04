import { SignedIn, SignedOut, RedirectToSignIn } from '@clerk/clerk-react';
import ClerkProviderWithRoutes  from './auth/ClerkProviderWithRoutes';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import {Layout} from "./layout/Layout.jsx"
import {AuthenticationPage} from './pages/AuthenticationPage';
import HomePage from './pages/HomePage';
import DashboardPage from './pages/DashboardPage';
import Navbar from './components/Navbar';
import './App.css';
import ContentCreator from './components/ContentCreator.jsx';


function App() {
    return (<ClerkProviderWithRoutes> 
      <Routes>
            <Route path="/sign-in/*" element={<AuthenticationPage />} />
            <Route path="/sign-up" element={<AuthenticationPage />} />
               <Route path="/" element={<HomePage />}/>
               <Route element={<Layout />}>
                <Route path="/Dashboard" element={<DashboardPage />}/>
                <Route path="/Content creator" element={<ContentCreator />} />
              </Route>
            
            
        </Routes>
    </ClerkProviderWithRoutes>
    );
}

export default App
