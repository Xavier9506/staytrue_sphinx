SDC-LE-A3H
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SDC-LE-A3的宽压版本，5V宽压支持，适应复杂供电环境，采用贴片+插针双安装方式，优化了电源管理，适合电池供电的便携设备。

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - .. image:: ../images/sdc-le-a3h-img1.png
         :width: 300
         :alt: SDC-LE-A3H 模组正面图
     - .. image:: ../images/sdc-le-a3h-img2.png
         :width: 300
         :alt: SDC-LE-A3H 模组反面图

.. image:: ../images/sdc-le-a3h-img3.png
   :width: 300
   :align: center
   :alt: SDC-LE-A3H 模组实物图

核心性能
~~~~~~~~~~
- 处理器：32位RISC-V内核，120MHz主频
- 存储：512KB Flash + 64KB SRAM + 8K cache
- 蓝牙射频：BLE5.4（QDID:222495），发射+9dBm，接收-94dBm
- 典型供电：2~4.5V（3.3V）
- 扩展功能：16引脚引出，支持UART/IIC/SPI、44按键矩阵扫描、Touch Key、LEDC幻彩灯驱动
- 特殊IO：2路高压IO（PA0/PA1），支持5V MCU通信
- 工作温度：-40℃~85℃
- 封装尺寸: 邮票孔封装，半孔间距1.27mm，尺寸27.5mm x 15mm

核心特性
~~~~~~~~~~
- 所有GPIO支持CrossBar任意映射，上电后软件配置即可切换功能
- 优化的电源管理，休眠电流低至10μA
- 邮票孔封装，半孔间距1.27mm，尺寸13×19mm