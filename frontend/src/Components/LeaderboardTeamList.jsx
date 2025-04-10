import React, {Component} from 'react';

class LeaderboardTeamList extends Component {

    constructor(props) {
        super(props);

        this.state = {
            teams : [
                {
                    name: 'Team A',
                    uni: 'UoM',
                    solvedProblems: 4,
                    totalRuntime: 545
                },
                {
                    name: 'Team B',
                    uni: 'Auth',
                    solvedProblems: 6,
                    totalRuntime: 359
                },
                {
                    name: 'Team C',
                    uni: 'UoM',
                    solvedProblems: 4,
                    totalRuntime: 407
                }
            ]
        }
    }

    sortByProbSolved = () => {
        const sorted = [...this.state.teams]
            .sort((a, b) => {
                if(a.solvedProblems !== b.solvedProblems) {
                    return b.solvedProblems - a.solvedProblems;
                }
                return a.totalRuntime - b.totalRuntime;
            });
        this.setState({teams: sorted});
    }

    componentDidMount() {
        this.sortByProbSolved();
    }

    componentDidCatch(error, errorInfo) {
        console.log(error, errorInfo);
    }

    render() {
        return (
            <div>
                <ul>
                    {this.state.teams.map((teams, index) => (
                        <li key={teams.name}>{index + 1}, {teams.name}, {teams.uni}, {teams.solvedProblems}, {teams.totalRuntime}</li>
                    ))}
                </ul>
            </div>
        );
    }
}

export default LeaderboardTeamList;