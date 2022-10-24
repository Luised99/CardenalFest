package com.example.db.config;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;

import com.mysql.jdbc.Driver;

@Configuration
public class DBConfig {
	
	private final String host;
	private final String user;
	private final String password;
	private final String port;
	private final String db;
	
	public DBConfig(@Value("${mysql.host") String host, @Value("${mysql.user") String user,
			@Value("${mysql.password") String password, @Value("${mysql.port") String port,
			@Value("${mysql.db") String db) {
		this.host=host;
		this.user=user;
		this.password=password;
		this.port=port;
		this.db=db;
	}
	
	public Connection conectar() {
		
		Connection con = null;
		
		try {
			Class.forName("com.mysql.jdbc.Driver");
			con = DriverManager.getConnection(  
					"jdbc:mysql://" + host + ":" + port + "/" + db,user,password);
		} catch (ClassNotFoundException | SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return con;
	}
}
