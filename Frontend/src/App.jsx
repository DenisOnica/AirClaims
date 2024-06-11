import { Routes, Route } from "react-router-dom";

import NavBar from "./Components/Navbar";
import Home from "./Pages/Home/Home";
import About from "./Pages/About/About";
import Aplica from "./Pages/Aplica/Aplica";
import Drepturi from "./Pages/Drepturi/Drepturi";
import Contact from "./Pages/Contact/Contact";

function App() {
  return (
    <>
      <NavBar color="white" textColor="black" />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/drepturi" element={<Drepturi />} />
        <Route path="/desprenoi" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/aplica" element={<Aplica />} />
      </Routes>
    </>
  );
}

export default App;
