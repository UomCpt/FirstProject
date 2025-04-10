import React, {Component} from 'react';
import LeaderboardTeamList from "./LeaderboardTeamList.jsx";

class LeaderboardWrapper extends Component {
    render() {
        return (
            <>
                <h1>UoM Hackathon 2026</h1>
                <LeaderboardTeamList/>
            </>
        );
    }
}

export default LeaderboardWrapper;