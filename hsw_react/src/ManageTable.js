//import 'bootstrap/dist/css/bootstrap.min.css';

import React, { useState, useEffect } from "react";
import { getManageApplication } from './api';
import TableRow from "./TableRow";
//import Table from 'react-bootstrap/Table'

const ManageTable = (props) => {
    const headerMeta = [
        "channel_title",
        "video_thumbnail"
    ];

    const [tableData, setTableData] = useState([getManageApplication(1)]);

    return (
        <>
        <h3>Manage Table</h3>
        <div>
            {tableData.length !== 0 && (
            <table>
                <thead>
                <tr>
                   {headerMeta.map(i=><th>{i}</th>)}
                </tr>
                </thead>
                <tbody>
                {tableData.map((d, i) => {
                    return (<TableRow key={i} data={d}/>);
                }
                )}
                </tbody>
            </table>
            )}
        </div>
        </>
    )
}

export default ManageTable;
