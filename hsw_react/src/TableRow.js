import React, { useState, useEffect } from "react";

const TableRow = ({ key, data}) => {
    const [RowData, setRowData] = useState(data);

    return (
        <>
        <tr key={key}>
            <td>{RowData.instance}</td>
            <td>{RowData.application}</td>
        </tr>
        </>
    )
};

export default TableRow;