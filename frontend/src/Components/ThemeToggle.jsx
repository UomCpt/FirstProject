import { Classic } from "@theme-toggles/react";
import "@theme-toggles/react/css/Classic.css";
import { useTheme } from "../context/ThemeContext"; // Make sure this path is correct
import { useEffect, useState } from 'react';

export default function ThemeToggle() {
  const { isDarkMode, toggleTheme } = useTheme(); // Get theme controls from context
  const [mounted, setMounted] = useState(false);
  
  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return (
    <ErrorBoundary fallback={<div>Toggle unavailable</div>}>
      <Classic 
        duration={750}
        toggled={isDarkMode}  // Connect to current theme state
        toggle={toggleTheme}   // Connect to toggle function
        style={{ fontSize: '2rem' }} // Make toggle larger
      />
    </ErrorBoundary>
  );
}

function ErrorBoundary({ children, fallback }) {
  const [hasError, setHasError] = useState(false);
  
  useEffect(() => {
    const handleError = () => setHasError(true);
    window.addEventListener('error', handleError);
    return () => window.removeEventListener('error', handleError);
  }, []);

  return hasError ? fallback : children;
}