#Import Flask, jsonify and request
import time 
import yaml
import datetime
from flask import Flask, jsonify, request
from cltBase.Api import Api

api = Api()


#run the web service    
app = Flask(__name__)

# Define the route and function for the web service
@app.route("/books")
def get_books():
        # Create a list of books
            #books = [
                #{"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "record_date": "2023-01-01"},
                #{"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "record_date": "2023-01-02"},
                #{"id": 3, "title": "1984", "author": "George Orwell", "record_date": "2023-01-03"}
            #]
            # Get the optional parameters from the query string
            #ecord_date = request.args.get("record_date")
    mac = request.args.get("mac")#,default=None)
            # Filter the books by record date and id if provided
            #f record_date:
                #ooks = [book for book in books if book["record_date"] == record_date]
    print("MAC", mac)
    if mac:
                #books = [book for book in books if book["id"] == int(id)]
        sql = f"SELECT * FROM CM_TEST_HISTORY t LEFT JOIN cable_modems_cpe_types ct ON t.cpe_type = ct.id LEFT JOIN CM_CURRENT_TEST c ON t.test_id = c.id LEFT JOIN clients_client cc on c.CLIENT_ID = cc.id LEFT JOIN CM_DIAGNOSTIC_LIST dl on dl.id = t.diagnostic WHERE t.MAC = '{mac}'"
        res = api.execute_sql(sql)
        if 'results' in res:
            rows = res['results']
            for i in range(0, len(rows)):
                row = rows[i]

        start_date = datetime.datetime.strptime(row["START_DATE"], "%Y-%m-%d %H:%M:%S")
        end_date = datetime.datetime.strptime(row["END_DATE"], "%Y-%m-%d %H:%M:%S")

        time_difference = end_date - start_date
        
        time_seconds = int(time_difference.total_seconds())


        data = [
            {
                "type": "api_auth",
                "api_key": "xlksduirerlidfsidf"
            },
            {
                "type": "test",
                "cpe_type": "stb",
                "test_id": row["TEST_ID"],
                "start_date": row["START_DATE"],
                "end_date": row["END_DATE"],
                "test_time": time_seconds,
                "operator": "ggarcia",
                "cpes": [
                    {
                        "ip": row["IP"],
                        "mac": row["MAC"],
                        "vendor": row["VENDOR"],
                        "model": row["MODEL"],
                        "serial": row["SERIAL"],
                        "reg_date": "",
                        "cpe_type": row["type_name"],
                        "data": {
                            "lan_mac": row["MAC"],
                            "mta_mac": row["MAC_MTA"],
                            "http_passwd": row["http_passwd"],
                            "docsis_file": "",
                            "client_name": row["name"],
                            "test_id": row["TEST_ID"]
                        },
                        "diagnostic": {
                            "code": row["CODE"],
                            "txt": row["DIAGNOSTIC"],
                            "custom_code": row["CODE"],
                            "custom_txt": row["CUSTOM_DIAGNOSTIC"]
                        },
                        "status": {
                            "test_saved": {
                                "_value": row["TEST_DATA"][207:209]
                            }
                        },
                        "wifi": {
                            "_value": row["WIFI"],
                            "bssid": row["wifi_network"],
                            "network": "",
                            "tx_power": row["RXPOWER"],
                            "mac": row["MAC"],
                            "down_status": row["TEST_DATA"][207:209]
                        },
                        "wifi5g": {
                            "_value": row["WIFI_5G_STATUS"],
                            "bssid": row["wifi_network"].replace("FIBRA", "PLUS"),
                            "tx_power": row["RXPOWER"],
                            "mac": row["MAC"],
                            "down_status": row["TEST_DATA"][207:209],
                            "network": ""
                        },
                        "download": {
                            "_value": row["SERVICE_DOWNLOAD_STATUS"],
                            "down_time": row["TEST_DATA"][115:123],
                            "down_size": row["TEST_DATA"][58:66]
                        },
                        "sw_upgr": {
                            "_value": row["STATUS"].replace("registrationComplete", "OK"),
                            "swv": row["SWV"],
                            "prev_swv": "",
                            "status_value": ""
                        },
                        "sip": {
                            "_value": row["SERVICE_SIP_STATUS"],
                            "last_time": "",
                            "lost_seconds": 60
                        }
                    }
                ]
            }
        ]  
        # Return the list of books as JSON
        #return jsonify(books)
        return jsonify(data)
# Run the web service
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

