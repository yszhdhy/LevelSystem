package com.xc.example.service.impl;

import org.springframework.stereotype.Service;
import java.util.Map;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;

import com.xc.example.mapper.HistoryTableDao;
import com.xc.model.model.HistoryTableEntity;
import com.xc.example.service.HistoryTableService;


@Service("historyTableService")
public class HistoryTableServiceImpl extends ServiceImpl<HistoryTableDao, HistoryTableEntity> implements HistoryTableService {


}
