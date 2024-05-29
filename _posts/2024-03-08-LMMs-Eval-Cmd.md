---
layout: post
title: LMMs Eval Command Generator
date: 2024-03-08
categories: Tools
tags:
  - tools
description: a simple tool to generate commands for LMMs-Eval
giscus_comments: true
related_posts: false
pretty_table: true
---

{% include scripts/jquery.liquid %}

## Select Models

<table
  id="models"
  class="table align-middle mb-0 bg-white"
  data-toggle="table"
  data-height="460"
  data-search="true"
  data-click-to-select="true"
  data-url="{{ 'assets/json/2024-03-08-LMMs-Eval-Cmd/models.json' | relative_url }}">
  <thead>
    <tr>
      <th data-field="state" data-checkbox="true"></th>
      <th data-field="Name" data-sortable="true">Name</th>
      <th data-field="ID" data-sortable="true">ID</th>
    </tr>
  </thead>
</table>

---

## Select Tasks

<table
  id="tasks"
  data-search="true"
  data-toggle="table"
  class="table align-middle mb-0 bg-white"
  data-height="460"
  data-click-to-select="true"
  data-url="{{ 'assets/json/2024-03-08-LMMs-Eval-Cmd/tasks.json' | relative_url }}">
  <thead>
    <tr>
      <th data-field="state" data-checkbox="true"></th>
      <th data-field="Name" data-sortable="true">Name</th>
      <th data-field="ID" data-sortable="true">ID</th>
    </tr>
  </thead>
</table>

---

## Enter Model Args

<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon1">Model Args</span>
  <input type="text" class="form-control" placeholder="pretrained=liuhaotian/llava-v1.5-7b" aria-label="model_args" aria-describedby="basic-addon1">
</div>

---

## Get Command

<figure class="highlight"><div class="code-display-wrapper"><pre><code class="language-bash" data-lang="bash">accelerate launch <span class="nt">-m</span> lmms_eval <span class="nt">--model</span><span class="o">=</span><span id="selectedModels"></span> <span class="nt">--model_args</span><span class="o">=</span><span id="modelArgs"></span> <span class="nt">--tasks</span><span class="o">=</span><span id="selectedTasks"></span> <span class="nt">--batch_size</span><span class="o">=</span>1 <span class="nt">--log_samples</span> <span class="nt">--output_path</span><span class="o">=</span>./logs/</code></pre></div></figure>

<script src="{{ 'assets/js/2024-03-08-LMMs-Eval-Cmd/script.js' | relative_url }}"></script>
