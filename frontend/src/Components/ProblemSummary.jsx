import React, {Component} from 'react';

class ProblemSummary extends Component {

    constructor(props) {
        super(props);

        this.state = {
            problems: [
                {
                    name: "A",
                    numOfSols: 5,
                    numOfFailSubmit: 6,
                    numOfPending: 20,
                    bestTime: 2
                },
                {
                    name: "B",
                    numOfSols: 3,
                    numOfFailSubmit: 18,
                    numOfPending: 40,
                    bestTime: 50
                },
                {
                    name: "C",
                    numOfSols: 4,
                    numOfFailSubmit: 3,
                    numOfPending: 10,
                    bestTime: 10
                }
            ]
        }
    }


    render() {
        return (
            <div>
                <div>
                    <ul>
                        {this.state.problems.map((problem) => (
                            <>
                                <h3>{problem.name}</h3>
                                <li key={problem.name}>{problem.numOfSols}, {problem.numOfFailSubmit}, {problem.numOfPending}, {problem.bestTime} ms</li>
                            </>
                        ))}
                    </ul>
                </div>
            </div>
        );
    }
}

export default ProblemSummary;