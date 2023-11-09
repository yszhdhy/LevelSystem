package com.xc.example.service.impl;

import org.springframework.stereotype.Service;
import java.util.Map;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;

import com.xc.example.mapper.QualifiedOrNotDao;
import com.xc.model.model.QualifiedOrNotEntity;
import com.xc.example.service.QualifiedOrNotService;


@Service("qualifiedOrNotService")
public class QualifiedOrNotServiceImpl extends ServiceImpl<QualifiedOrNotDao, QualifiedOrNotEntity> implements QualifiedOrNotService {


}
