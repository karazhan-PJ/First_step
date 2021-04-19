import React, { useState, useEffect } from "react";

import 'bootstrap/dist/css/bootstrap.min.css';
import Table from 'react-bootstrap/Table'
import Button from 'react-bootstrap/Button';

import { getManageApplication } from './api';
import TableRow from "./TableRow";


// JenkIns 배포 테스트
const ManageTable = (props) => {
    const headerMeta = [
        "channel_title",
        "video_thumbnail"
    ];

    const [tableData, setTableData] = useState([]);

    let input = null;
    const change = (e) => {
       input = e.target.value;
    }

    const appChange = () => {
        let result = getManageApplication(input);
        setTableData([result]);
    }

    return (
        <>
        <Button variant="primary" onClick={appChange}>전송1</Button>{' '}
        <input type="text" onChange={change} />

        <h3>Manage Table</h3>
        <div>
            {tableData.length !== 0 && (
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            {headerMeta.map(i=><th>{i}</th>)}
                        </tr>
                    </thead>
                    <tbody>
                        {tableData.map(d => {
                            return (<TableRow data={d}/>);
                        }
                        )}
                    </tbody>
                </Table>
            )}
        </div>
        </>
    )
}

export default ManageTable;
