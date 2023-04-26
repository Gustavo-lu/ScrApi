indexHtml = """
<!DOCTYPE html>
<html>
  <head>
    <script
      src="https://unpkg.com/react@18/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"
      crossorigin
    ></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <div id="mainApp"></div>

    <script type="text/babel">
      const { useState, useEffect } = React;
      const url = window.location.protocol +"//"+window.location.host;
        function App() {
          const [number, setNumber] = useState(null);
          const [data, setData] = useState(null);
      console.log(url)
          function getData() {

            axios
              .get(`${url}/scrapi/coin/${number}`)
              .then(function (response) {
                setData(JSON.stringify(response.data));
              })
              .catch(function (error) {
                console.log(error);
              });
          }

          return (
            <div className="flex flex-col items-center justify-center h-screen bg-gray-900">
              <div className="bg-rose-600 p-12 rounded-lg flex flex-col items-center justify-center">
                <h1 className="text-2xl font-bold mb-4 text-center text-slate-50">
                  ScrApi
                </h1>
                <input
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="number"
                  onChange={(e) => {
                    setNumber(e.nativeEvent.data);
                  }}
                />
                {data&&<pre className="bg-gray-900 py-5 px-[5rem] rounded mt-4"><p className="text-lime-500">{data}</p></pre>}
                <button
                  onClick={getData}
                  className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mx-auto mt-4"
                >
                  Buscar
                </button>


              </div>
            </div>
          );
        }

        const container = document.getElementById("mainApp");
        const root = ReactDOM.createRoot(container);
        root.render(<App />);
    </script>
  </body>
</html>


    """