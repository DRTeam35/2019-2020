package sample;

import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.Arrays;

import org.json.simple.*;

public class Server {
    private final Socket socket;
    private final Camera camera = new Camera();

    private byte[] cameraData;
    private ArrayList<String> sensorData;

    public Server(int port) throws IOException {
        //Start a server at initialization
        ServerSocket serverSocket = new ServerSocket(port);
        System.out.println("The server has been started, waiting for connection...");
        socket = serverSocket.accept();
        System.out.println( "The Client "+ socket.getInetAddress() + " : " + socket.getPort() + " is connected");
    }

    public void receiveData() throws IOException {
        //Receive data from client
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String response;
            while ((response = bufferedReader.readLine()) != null) {
                JSONObject jsonObject = (JSONObject) JSONValue.parse(response); //Parse incoming json data
                JSONArray cameraArray = (JSONArray) jsonObject.get("camera");
                JSONArray sensorArray = (JSONArray) jsonObject.get("sensors");

                this.sensorData = this.convertSensorData(sensorArray);
                this.cameraData = camera.transformToByteArray(cameraArray);
            }
        System.out.println("No connection");
    }

    public void sendData() throws IOException {
        //Send data, only a string for now
        PrintStream printStream = new PrintStream(socket.getOutputStream());
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));

        String messageToSend;
        try{
            while((messageToSend = keyboard.readLine()) != null){
                printStream.println(messageToSend);
                System.out.println("Message Sent: " + messageToSend);
            }
        }catch (SocketException socketException){
            System.out.println("Connection lost...");
            socketException.printStackTrace();
        }
    }

    private ArrayList<String> convertSensorData(JSONArray sensorArray){
        ArrayList<String> sensorValues = new ArrayList<>();
        for(Object object : sensorArray.toArray()){
            String value = object.toString();
            sensorValues.add(value);
        }
        return sensorValues;
    }

    public void sendPingRequest(String ipAddress) throws IOException {
        InetAddress inetAddress = InetAddress.getByName(ipAddress);
        System.out.println("Sending Ping Request to " + ipAddress);
        if (inetAddress.isReachable(5000))
            System.out.println("Reached!");
        else
            System.out.println("Unable to reach");

    }

    public byte[] getCameraData() {
        return cameraData;
    }

    public ArrayList<String> getSensorData() {
        return sensorData;
    }
}
