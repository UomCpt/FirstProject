import React, {Component} from 'react';

class ScrollToTopBtn extends Component {
    constructor(props) {
        super(props);

        this.state = {
            visible: false
        };
    }

    componentDidMount() {
        window.addEventListener("scroll", this.toggleVisible);
    }

    componentWillUnmount() {
        window.removeEventListener("scroll", this.toggleVisible);
    }

    toggleVisible = () => {
        if(window.scrollY > 300) {
            this.setState({
                visible: true
            });
        } else {
            this.setState({
                visible: false
            });
        }
    }

    scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }

    render() {
        return (
            <div>
                {this.state.visible || (
                    <button onClick={this.scrollToTop}>
                        go to top
                    </button>
                )}
            </div>
        );
    }
}

export default ScrollToTopBtn;