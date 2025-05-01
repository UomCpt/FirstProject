import React, {Component} from 'react';
import LeaderboardTeamList from "./LeaderboardTeamList.jsx";
import ProblemSummary from "./ProblemSummary.jsx";

class LeaderboardWrapper extends Component {
    render() {
        return (
            <>
                <h1>UoM Hackathon 2026</h1>
                <div className="leaderboardContainer">
                    <LeaderboardTeamList/>
                    <ProblemSummary/>
                </div>
            </>
        );
    }
}

export default LeaderboardWrapper;