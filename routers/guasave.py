from mysql.connector import Error
from connection import connection, disconnection
from fastapi import APIRouter

router = APIRouter(
    prefix="/guasave",
    tags=["guasave"],
    responses={404: {"description": "Not found"}})

@router.get("/")
def getCalls():
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr;")
        cursor.execute(query)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                call_dict = {
                    "calldate": date,
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/bydate")
def getDate(startDate, endDate):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where calldate between %s and %s;")
        val = (startDate, endDate,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                call_dict = {
                    "calldate": date,
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/bySrc")
def getSrc(src):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where src = %s;")
        val = (src,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                call_dict = {
                    "calldate": date,
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/byDst")
def getDst(dst):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where dst = %s;")
        val = (dst,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                call_dict = {
                    "calldate": date,
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/byStatus")
def getStatus(status):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where disposition = %s;")
        val = (status,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                call_dict = {
                    "calldate": date,
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)