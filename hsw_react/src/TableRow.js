import React, { useState, useEffect } from "react";

const TableRow = ({ key, data}) => {
    const [RowData, setRowData] = useState(data);

    return (
        <>
        <tr key={key}>
            <td><img src={RowData.thumbnail} class="thumbnail"/></td>
            <td>{RowData.title}</td>
        </tr>
        </>
    )
};

export default TableRow;