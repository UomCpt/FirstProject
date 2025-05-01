import React, { Component } from "react";

class LeaderboardTeamList extends Component {
    constructor(props) {
        super(props);

        this.state = {
            teams: [
                {
                    name: "Team A",
                    uni: "UoM",
                    solvedProblems: 4,
                    totalRuntime: 545
                },
                {
                    name: "Team B",
                    uni: "Auth",
                    solvedProblems: 6,
                    totalRuntime: 359
                },
                {
                    name: "Team C",
                    uni: "UoM",
                    solvedProblems: 4,
                    totalRuntime: 407
                }
            ]
        };
    }

    sortByProbSolved = () => {
        const sorted = [...this.state.teams].sort((a, b) => {
            if (a.solvedProblems !== b.solvedProblems) {
                return b.solvedProblems - a.solvedProblems;
            }
            return a.totalRuntime - b.totalRuntime;
        });
        this.setState({ teams: sorted });
    };

    componentDidMount() {
        this.sortByProbSolved();
    }

    componentDidCatch(error, errorInfo) {
        console.log(error, errorInfo);
    }

    render() {
        return (
            <div>
                <h2>Leaderboard</h2>
                <table
                    border="1"
                    cellPadding="8"
                    style={{ borderCollapse: "collapse", width: "100%" }}
                >
                    <thead>
                    <tr>
                        <th>place</th>
                        <th>Team </th>
                        <th>Score/Time</th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.state.teams.map((team, index) => (
                        <tr key={team.name}>
                            <td>{index + 1}</td>
                            <td>
                                <strong>{team.name}</strong>
                                <br />
                                <small>{team.uni}</small>
                            </td>
                            <td>
                                {team.solvedProblems} problems
                                <br />
                                {team.totalRuntime} ms
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        );
    }
}

export default LeaderboardTeamList;