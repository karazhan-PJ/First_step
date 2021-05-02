import React, { useState, useEffect } from "react";

const TableRow = ({key,data}) => {

    const [RowData, setRowData] = useState(data);

    useEffect(() => {
        setRowData(data);
    });

    return (
        <>
        <tr>
            <td><img src={RowData.thumbnail} id="thumbnail"/></td>
            <td>{RowData.title}</td>
        </tr>
        </>
    )
};

export default TableRow;