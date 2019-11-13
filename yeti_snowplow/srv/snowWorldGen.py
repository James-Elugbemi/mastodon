import os

worldStr = """<sdf version='1.6'>
  <world name='default'>
    <light name='sun' type='directional'>
      <cast_shadows>1</cast_shadows>
      <pose frame=''>0 0 10 0 -0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.1 0.1 0.1 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.5 -1</direction>
    </light>
    <gravity>0 0 -9.8</gravity>
    <magnetic_field>6e-06 2.3e-05 -4.2e-05</magnetic_field>
    <atmosphere type='adiabatic'/>
    <physics name='default_physics' default='0' type='ode'>
      <max_step_size>0.01</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>100</real_time_update_rate>
    </physics>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
    </scene>
    <spherical_coordinates>
      <surface_model>EARTH_WGS84</surface_model>
      <latitude_deg>0</latitude_deg>
      <longitude_deg>0</longitude_deg>
      <elevation>0</elevation>
      <heading_deg>0</heading_deg>
    </spherical_coordinates>
    <model name='brick_plane'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>100</mu>
                <mu2>50</mu2>
              </ode>
              <torsional>
                <ode/>
              </torsional>
            </friction>
            <contact>
              <ode/>
            </contact>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='visual'>
          <cast_shadows>0</cast_shadows>
          <pose frame=''>0 0 -0.04 0 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://brick_plane/meshes/BrickRoad.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>-0.145559 -0.040486 0 0 -0 0</pose>
    </model>
    <light name='user_point_light_0' type='point'>
      <pose frame=''>-40.2877 36.9378 1 0 -0 0</pose>
      <diffuse>0.5 0.5 0.5 1</diffuse>
      <specular>0.1 0.1 0.1 1</specular>
      <attenuation>
        <range>20</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>0</cast_shadows>
      <direction>0 0 -1</direction>
    </light>
    <light name='user_point_light_0_clone' type='point'>
      <pose frame=''>-43.3445 16.5003 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_0' type='point'>
      <pose frame=''>-41.8744 -4.62896 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_1' type='point'>
      <pose frame=''>-45.3384 -27.6087 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_2' type='point'>
      <pose frame=''>-41.0308 -51.4934 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_3' type='point'>
      <pose frame=''>-13.091 -48.6057 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_4' type='point'>
      <pose frame=''>17.8273 -50.2126 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_5' type='point'>
      <pose frame=''>43.0105 -50.5018 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_6' type='point'>
      <pose frame=''>-30.8096 43.6215 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_7' type='point'>
      <pose frame=''>-6.06965 44.6895 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_8' type='point'>
      <pose frame=''>12.7263 46.5664 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_9' type='point'>
      <pose frame=''>31.1126 44.5953 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_10' type='point'>
      <pose frame=''>48.6896 31.6 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_11' type='point'>
      <pose frame=''>54.0783 8.97523 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_12' type='point'>
      <pose frame=''>59.1715 -20.1842 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <light name='user_point_light_0_clone_13' type='point'>
      <pose frame=''>56.6391 -41.8663 10 0 -0 0</pose>
      <diffuse>1 1 1 1</diffuse>
      <specular>1 1 1 1</specular>
      <direction>0 0 -1</direction>
      <attenuation>
        <range>100000</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    
    
    
    
    
    
    
    
    <state world_name='default'>
      <sim_time>0 0</sim_time>
      <real_time>0 0</real_time>
      <wall_time>1545495050 494732236</wall_time>
      <iterations>0</iterations>
	  <model name='person_standing'>
        <pose frame=''>-9.80604 -1.11962 0 0 1e-06 1.77539</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>-9.80604 -1.11962 0 0 1e-06 1.77539</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>1.94081 -1.83425 1.44474 -1.32942 0.997975 -3.09681</acceleration>
          <wrench>155.264 -146.74 115.579 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone'>
        <pose frame=''>-13.8864 -3.88541 0 -1e-06 1e-06 1.76835</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>-13.8864 -3.88541 0 -1e-06 1e-06 1.76835</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>1.95716 -1.87577 1.61322 -1.28813 0.980639 -3.09743</acceleration>
          <wrench>156.573 -150.062 129.058 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_0'>
        <pose frame=''>-14.4559 -2.3232 -1e-06 -1e-06 2e-06 1.7688</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>-14.4559 -2.3232 -1e-06 -1e-06 2e-06 1.7688</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>-1.47131 1.3979 -1.2609 1.74141 -1.54444 3.09671</acceleration>
          <wrench>-117.704 111.832 -100.872 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_1'>
        <pose frame=''>-14.3848 -0.350336 -1e-06 -1e-06 1e-06 1.76419</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>-14.3848 -0.350336 -1e-06 -1e-06 1e-06 1.76419</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>-1.43978 1.38245 -1.43447 -1.3607 -1.54352 -0.031124</acceleration>
          <wrench>-115.183 110.596 -114.758 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_2'>
        <pose frame=''>-14.429 1.55852 0 1e-06 1e-06 1.76449</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>-14.429 1.55852 0 1e-06 1e-06 1.76449</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>-1.05314 -2.4493 1.42274 2.44021 -1.31512 -0.287452</acceleration>
          <wrench>-84.2513 -195.944 113.819 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_3'>
        <pose frame=''>13.2726 6.42799 0 -1e-06 1e-06 -1.39375</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>13.2726 6.42799 0 -1e-06 1e-06 -1.39375</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>-1.8932 1.89069 1.46466 1.27056 -1.04771 -3.09659</acceleration>
          <wrench>-151.456 151.255 117.173 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_4'>
        <pose frame=''>15.3448 5.20997 0 0 1e-06 1.77559</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>15.3448 5.20997 0 0 1e-06 1.77559</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>1.90163 -1.85625 1.53447 -1.30283 0.990869 3.0587</acceleration>
          <wrench>152.131 -148.5 122.758 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_5'>
        <pose frame=''>15.5596 2.80858 0 1e-06 -1e-06 1.75761</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>15.5596 2.80858 0 1e-06 -1e-06 1.75761</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>1.39584 -1.35614 -1.60894 1.36101 1.51766 -0.043692</acceleration>
          <wrench>111.667 -108.491 -128.715 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_6'>
        <pose frame=''>15.1253 0.11685 0 0 -1e-06 1.76058</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>15.1253 0.11685 0 0 -1e-06 1.76058</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>1.08337 2.43111 1.4055 -2.4601 1.25311 -0.045425</acceleration>
          <wrench>86.6698 194.489 112.44 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_7'>
        <pose frame=''>14.7562 -3.10187 0 1e-06 -1e-06 1.75761</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>14.7562 -3.10187 0 1e-06 -1e-06 1.75761</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>1.39584 -1.35614 -1.60894 1.36101 1.51766 -0.043692</acceleration>
          <wrench>111.667 -108.491 -128.715 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_8'>
        <pose frame=''>13.2298 -6.32983 0 1e-06 1e-06 1.77703</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>13.2298 -6.32983 0 1e-06 1e-06 1.77703</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>-1.04443 -2.45143 1.41842 2.4826 -1.21239 -0.045342</acceleration>
          <wrench>-83.5542 -196.114 113.473 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_standing_clone_9'>
        <pose frame=''>12.7298 -8.89016 0 -0 1e-06 1.76611</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>12.7298 -8.89016 0 -0 1e-06 1.76611</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>1.78557 -1.85634 1.34146 -1.30303 1.12085 3.09802</acceleration>
          <wrench>142.845 -148.507 107.317 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_walking'>
        <pose frame=''>11.0009 7.91802 0 0 1e-06 0.002189</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>11.0009 7.91802 0 0 1e-06 0.002189</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>-1.41032 -0.007256 0.494449 0.007857 -1.48457 -6.1e-05</acceleration>
          <wrench>-112.826 -0.580497 39.5559 0 -0 0</wrench>
        </link>
      </model>
      <model name='person_walking_0'>
        <pose frame=''>-4.63638 -8.9191 0 0 -1e-06 1.61285</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>-4.63638 -8.9191 0 0 -1e-06 1.61285</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>-0.063873 1.40888 0.494368 -1.6583 -0.067382 -5.1e-05</acceleration>
          <wrench>-5.10983 112.711 39.5494 0 -0 0</wrench>
        </link>
      </model>
      <light name='sun'>
        <pose frame=''>0 0 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0'>
        <pose frame=''>-40.2877 36.9378 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone'>
        <pose frame=''>-43.3445 16.5003 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_0'>
        <pose frame=''>-41.8744 -4.62896 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_1'>
        <pose frame=''>-45.3384 -27.6087 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_10'>
        <pose frame=''>48.6896 31.6 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_11'>
        <pose frame=''>54.0783 8.97523 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_12'>
        <pose frame=''>59.1715 -20.1842 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_13'>
        <pose frame=''>56.6391 -41.8663 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_2'>
        <pose frame=''>-41.0308 -51.4934 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_3'>
        <pose frame=''>-13.091 -48.6057 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_4'>
        <pose frame=''>17.8273 -50.2126 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_5'>
        <pose frame=''>43.0105 -50.5018 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_6'>
        <pose frame=''>-30.8096 43.6215 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_7'>
        <pose frame=''>-6.06965 44.6895 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_8'>
        <pose frame=''>12.7263 46.5664 10 0 -0 0</pose>
      </light>
      <light name='user_point_light_0_clone_9'>
        <pose frame=''>31.1126 44.5953 10 0 -0 0</pose>
      </light>
      <model name='yeti'>
        <pose frame=''>0 0 0 0 0 0</pose><!-- 0 0 0 is on the ground or atleast looks like it-->
        <scale>1 1 1</scale>
        <link name='chassis'>
          <pose frame=''>0 0 0 0 0 0</pose>
          <velocity>0 0 0 0 0 0</velocity>
          <acceleration>0 0 0 0 0 0</acceleration>
          <wrench>0 0 0 0 0 0</wrench>
        </link>
        <link name='left_back_wheel'>
          <pose frame=''>0 0 0 0 0 0</pose>
          <velocity>0 0 0 0 0 0</velocity>
          <acceleration>0 0 0 0 0 0</acceleration>
          <wrench>0 0 0 0 0 0</wrench>
        </link>
        <link name='left_front_wheel'>
          <pose frame=''>0 0 0 0 0 0</pose>
          <velocity>0 0 0 0 0 0</velocity>
          <acceleration>0 0 0 0 0 0</acceleration>
          <wrench>0 0 0 0 0 0</wrench>
        </link>
        <link name='right_back_wheel'>
          <pose frame=''>0 0 0 0 0 0</pose>
          <velocity>0 0 0 0 0 0</velocity>
          <acceleration>0 0 0 0 0 0</acceleration>
          <wrench>0 0 0 0 0 0</wrench>
        </link>
        <link name='right_front_wheel'>
          <pose frame=''>0 0 0 0 0 0</pose>
          <velocity>0 0 0 0 0 0</velocity>
          <acceleration>0 0 0 0 0 0</acceleration>
          <wrench>0 0 0 0 0 0</wrench>
        </link>
      </model>
"""

worldStr2 = """        </state>
        
        
        
        <gui fullscreen='0'>
            <camera name='user_camera'>
                <pose frame=''>-14.9349 -8.57665 12.7876 0 0.809671 0.957132</pose>
                <view_controller>orbit</view_controller>
                <projection_type>perspective</projection_type>
            </camera>
        </gui>
        <model name='single-I'>
          <include>
            <uri>model://single-I</uri>
          </include>
          <pose frame=''>6 -2 .03 0 0 0</pose>
        </model>
        <model name='yeti'>
          <include>
            <uri>model://yeti_with_plow</uri>
          </include>
          <pose frame=''>0 0 0 0 0 0</pose>
        </model>
        <model name='pylon_yellow'>
          <include>
            <uri>model://pylon_yellow</uri>
          </include>
          <pose frame=''>5 0 0 0 0 0</pose>
        </model>
        <model name='pylon_orange'>
          <include>
            <uri>model://pylon_orange</uri>
          </include>
          <pose frame=''>7.5 1 0 0 0 0</pose>
        </model>
        <!--<model name='person_standing'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>-9.80619 -1.11871 0 0 -0 0</pose>
    </model>
    <model name='person_standing_clone'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>-13.8864 -3.88519 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_0'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>-14.456 -2.32294 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_1'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>-14.3848 -0.350533 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_2'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>-14.429 1.55837 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_3'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>11.1931 2.12797 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_4'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>15.3446 5.2109 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_5'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>15.5597 2.80775 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_6'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>15.1254 0.116322 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_7'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>14.7563 -3.1027 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_8'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>13.2296 -6.32877 0 0 -0 1.76606</pose>
    </model>
    <model name='person_standing_clone_9'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 -0.1 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>24.88</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>25.73</iyy>
            <iyz>0</iyz>
            <izz>2.48</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 -0.1 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.5 0.35 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 0.02 0.04 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_standing/meshes/standing.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>12.7298 -8.89016 0 0 -0 1.76606</pose>
    </model>
    <model name='person_walking'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 0 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>27.82</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>24.88</iyy>
            <iyz>0</iyz>
            <izz>4.57</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 0 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.35 0.75 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 -0.02 0 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_walking/meshes/walking.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 -0.02 0 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_walking/meshes/walking.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>11.0009 7.91801 0 0 -0 0</pose>
    </model>
    <model name='person_walking_0'>
      <link name='link'>
        <inertial>
          <pose frame=''>0 0 0.95 0 -0 0</pose>
          <mass>80</mass>
          <inertia>
            <ixx>27.82</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>24.88</iyy>
            <iyz>0</iyz>
            <izz>4.57</izz>
          </inertia>
        </inertial>
        <collision name='bottom'>
          <pose frame=''>0 0 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.35 0.75 0.02</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='person'>
          <pose frame=''>0 0 -0.02 0 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_walking/meshes/walking.dae</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <pose frame=''>0 0 -0.02 0 -0 0</pose>
          <geometry>
            <mesh>
              <uri>model://person_walking/meshes/walking.dae</uri>
            </mesh>
          </geometry>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>-4.63638 -8.91908 0 0 -0 0</pose>
    </model>-->
"""

startStr = """        <model name='"""
middleStr = """'>
            <pose frame=''>"""
endStr = """ 0 0 0</pose>
            <link name='link'>
                <inertial>
                    <mass>"""
endStr1 = """</mass>
          <inertia>
            <ixx>0.145833</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.145833</iyy>
            <iyz>0</iyz>
            <izz>0.125</izz>
          </inertia>
        </inertial>
        <collision name='collision'>
          <geometry>
            <cylinder>
              <radius>.05</radius>
              <length>0.04</length>
            </cylinder>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <geometry>
            <cylinder>
              <radius>.083333</radius>
              <length>0.05</length>
            </cylinder>
          </geometry>
          <!--<material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>file://media/materials/scripts/gazebo.material</uri>
            </script>
          </material>-->
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
    </model>
"""
worldEndStr = """    </world>
</sdf>"""

defaultStr = """        <model name='"""
defaultStr2 = """'>
            <pose frame=''>"""
defaultStr3 = """ 0 0 0</pose>
            <scale>1 1 1</scale>
            <link name='link'>
                <pose frame=''>"""
defaultStr4 = """ 0 0 0</pose>
                <velocity>0 0 0 0 0 0</velocity>
                <acceleration>0 0 -9.8 0 0 0</acceleration>
                <wrench>0 0 -9.8 0 0 0</wrench>
            </link>
        </model>
"""

f = open("single-I_nosnow.sdf", "w")
f.write(worldStr)

maxX = 60
maxY = 6
maxZ = 1
scale = (1.0/6)
mass = 0.01# should be 1.38888 if i can do maths

for x in range(0,maxX):
    for y in range(0,maxY):
        for z in range(0,maxZ):#height of snow in cm
            pose = str(str(round(1.5+(1.0/12) + (x*scale),2)) + ' ' + str(round(-.5+(1.0/12) + (y*scale) + (0.01*((-1)**(x+1))),2)) + ' ' + str(.05+round((z)*scale,2)) + ' ')
            name = 'SnowPuck' + '-' + str(x) + '-' + str(y) + '-' + str(z)
            if(x>18 and x<23 and y>1 and y<6):
                continue
            f.write(defaultStr + name + defaultStr2 + pose + defaultStr3 + pose + defaultStr4);
f.write(worldStr2)
for x in range(0,maxX):
    print(str((0.01*((-1)**(x+1)))))
    for y in range(0,maxY):
        for z in range(0,maxZ):#height of snow in cm
            pose = str(str(round(1.5+(1.0/12) + (x*scale) ,2)) + ' ' + str(round(-.5+(1.0/12) + (y*scale) + (0.01*((-1)**(x+1))),2)) + ' ' + str(.05+round((z)*scale,2)) + ' ')
            name = 'SnowPuck' + '-' + str(x) + '-' + str(y) + '-' + str(z)
            if((x>18) and (x<23) and (y>0) and (y<5)):
                continue
            f.write(startStr + name + middleStr + pose + endStr + str(mass) + endStr1);
f.write(worldEndStr)
print("Done")
