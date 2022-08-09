// Create a display component class for coal page and export it
// ===============================================================
//
// Import React and ReactDOM
import React from 'react';
import ReactDOM from 'react-dom';


// Create display component class
class Display extends React.Component {
    // Add a componentDidMount() lifecycle method
    componentDidMount() {
        // Set the width of the div to the width of the browser window
        ReactDOM.findDOMNode(this).style.width = window.innerWidth + 'px';
    }
}

// readin data from backend in json format and display it in the display component
componentWillMount()
{
    // Read the data from the backend
    fetch('/api/coal')
        .then(response => response.json())
        .then(data => {
            // Set the state of the component with the data
            this.setState({
                data: data
            });
        });
}

// if the data changes, update the display component
componentWillUpdate(nextProps, nextState)
{
    // Update the display component
    ReactDOM.findDOMNode(this).style.width = window.innerWidth + 'px';
}


// Render the display component
render()
{
    return (
        <div>
            <h1>Display</h1>
            <p>This is the display page.</p>
        </div>
    );
}

// Export the display component class
export default Display;
// ===============================================================
// ===============================================================


