import { useEffect } from "react";

const useScript = (url) => {
  useEffect(() => {
    const script = document.createElement("script");

    window.__be = window.__be || {};
    window.__be.id = "5f6e9c07aaa01e00066392cb";
    var be = document.createElement("script");
    be.type = "text/javascript";
    be.async = true;
    be.src =
      ("https:" === document.location.protocol ? "https://" : "http://") +
      "cdn.chatbot.com/widget/plugin.js";
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(be, s);

    document.body.appendChild(script);
    return () => {
      document.body.removeChild(script);
    };
  }, [url]);
};
export default useScript;
